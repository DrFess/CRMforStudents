import requests

from aiogram import Router
from aiogram.filters.text import Text
from aiogram.types import Message, CallbackQuery, PollAnswer
from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

from bots.keybords.kb import (
    test_result,
    start_test,
    next_question,
    menu
)


router = Router()


class Testing(StatesGroup):
    start = State()
    poll = State()
    question = State()
    answer = State()
    finish = State()


@router.message(Text(text='Тест по теме занятия'))
async def get_theme_questions(message: Message, state: FSMContext):
    response = requests.get('http://localhost:8000/api/v1/test_categories/all')
    builder = InlineKeyboardBuilder()
    for category in response.json():
        builder.row(
            InlineKeyboardButton(
                text=category['title'],
                callback_data=f'theme {category["id"]}'
            )
        )
    await message.answer('Выберите тему', reply_markup=builder.as_markup())
    await state.set_state(Testing.start)
    await state.update_data(
        student_id=message.from_user.id,
        date=message.date.today().strftime('%Y-%m-%d')
    )


@router.callback_query(Testing.start)
async def get_questions(callback: CallbackQuery, state: FSMContext):
    data = callback.data.split(' ')
    response = requests.get('http://localhost:8000/api/v1/test_by_categorie', data=f'{data[1]}')
    questions = response.json()

    await state.update_data(
        questions=questions,
        theme=data[1],
        count=0
    )
    await callback.message.answer('Начать тест?', reply_markup=start_test)
    await state.set_state(Testing.poll)


@router.message(Testing.poll, Text(text=['Начать тест', 'Следующий вопрос']))
async def ask_question(message: Message, state: FSMContext):
    data = await state.get_data()

    if data['count'] <= (len(data['questions']) - 1):
        serial_number = data['count']

        question = data['questions']

        question_text = question[serial_number]['text']
        options = [question[serial_number]['answer_1'], question[serial_number]['answer_2'],
                   question[serial_number]['answer_3'], question[serial_number]['answer_4']]
        await message.answer_poll(
            question=question_text,
            options=options,
            is_anonymous=False,
            reply_markup=next_question
        )

        await state.update_data(
            correct_answer=question[serial_number]['correct_answer'],
            text=question_text,
            count=data['count'] + 1
        )

        await state.set_state(Testing.question)

    else:
        await message.answer('Вопросы по теме закончились', reply_markup=test_result)
        await state.set_state(Testing.finish)


@router.poll_answer(Testing.question)
async def answer_poll(answer: PollAnswer, state: FSMContext):
    await state.update_data(student_answer=answer.option_ids[0] + 1)
    data = await state.get_data()
    requests.post('http://localhost:8000/api/v1/add_student_answer', json=data)
    await state.set_state(Testing.poll)


@router.message(Testing.finish, Text(text='Покажи результат'))
async def total(message: Message, state: FSMContext):
    state_data = await state.get_data()
    data = {
        'student_id': state_data['student_id'],
        'theme_id': int(state_data['theme']),
        'date': state_data['date'],
    }
    response = requests.get('http://localhost:8000/api/v1/get_student_result', json=data)
    result = response.json()['result']
    if result > 100:
        await message.answer('Что-то пошло не так. Обратись к преподавателю')
    else:
        await message.answer(f'Правильных ответов {result}%', reply_markup=menu)
    await state.clear()
