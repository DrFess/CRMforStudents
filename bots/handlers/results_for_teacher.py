import requests

from aiogram import Router
from aiogram.filters import Text
from aiogram.types import Message, InlineKeyboardButton, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from aiogram3_calendar import SimpleCalendar

from bots.keybords.kb import (
    date_or_not_date,
    yes_or_no,
    menu_for_teacher,
    show_calendar,
    show_answers
)

router = Router()


class StepsResults(StatesGroup):
    group_step = State()
    no_date_step = State()
    calendar_step = State()
    date_step = State()
    answers_step = State()


@router.message(Text(text='Получить результат тестирования'))
async def select_group(message: Message, state: FSMContext):
    response = requests.get('http://localhost:8000/api/v1/get_groups').json()
    builder = InlineKeyboardBuilder()
    for group in response:
        builder.add(InlineKeyboardButton(
            text=f'{group["group_number"]}',
            callback_data=group['id']
        ))
    await message.answer('Выбери группу:', reply_markup=builder.as_markup())
    await state.set_state(StepsResults.group_step)


@router.callback_query(StepsResults.group_step)
async def get_results_group(callback: CallbackQuery, state: FSMContext):
    await state.update_data(
        group_number_id=callback.data
    )
    await callback.message.answer(
        f'Выбрана группа {callback.data}. Ищем по дате или по всем тестам?',
        reply_markup=date_or_not_date
    )


@router.message(StepsResults.group_step)
async def choose_step(message: Message, state: FSMContext):
    if message.text == 'По дате':
        await message.answer('Показать календарь?', reply_markup=show_calendar)
        await state.set_state(StepsResults.calendar_step)

    else:
        await message.answer(f'Показать результаты за всё время для студентов группы?', reply_markup=show_answers)
        await state.set_state(StepsResults.no_date_step)


@router.message(StepsResults.calendar_step)
async def show_calendar(message: CallbackQuery, state: FSMContext):
    await message.answer('Выбери дату:', reply_markup=await SimpleCalendar().start_calendar())
    await state.set_state(StepsResults.date_step)


@router.callback_query(StepsResults.date_step)
async def get_results_date(callback_query: CallbackQuery, state: FSMContext):
    date = callback_query.data.split(':')
    year = date[2]
    month = date[3]
    day = date[4]
    await state.update_data(
        year=year,
        month=month,
        day=day
    )
    await callback_query.message.answer(f'Выбранная дата {day}.{month}.{year}. Верно?', reply_markup=yes_or_no)
    await state.set_state(StepsResults.answers_step)


@router.message(StepsResults.answers_step)
async def get_results(message: Message, state: FSMContext):
    state_data = await state.get_data()
    response = requests.get(
        'http://localhost:8000/api/v1/get_profiles_by_parameter',
        data=state_data['group_number_id']
    ).json()
    answer = ''
    for student in response:
        data = {
            'total_student_id': f'{student["telegram_id"]}',
            'total_date': f'{state_data["year"]}-{state_data["month"]}-{state_data["day"]}',
        }
        response_1 = requests.get('http://localhost:8000/api/v1/total_student_answers', json=data)
        answer += f"{student['surname']} {student['name']}: {response_1.json()['result']}\n"
    await message.answer(answer, reply_markup=menu_for_teacher)
    await state.clear()


@router.message(StepsResults.no_date_step)
async def get_results_no_date(message: Message, state: FSMContext):
    state_data = await state.get_data()
    response = requests.get(
        'http://localhost:8000/api/v1/get_profiles_by_parameter',
        data=state_data['group_number_id']
    ).json()
    answer = ''
    for student in response:
        data = {'total_student_id': f'{student["telegram_id"]}'}
        response_1 = requests.get('http://localhost:8000/api/v1/get_students_result_without_date', json=data)
        answer += f"{student['surname']} {student['name']}: {response_1.json()['result']}\n"
    await message.answer(answer, reply_markup=menu_for_teacher)
    await state.clear()
