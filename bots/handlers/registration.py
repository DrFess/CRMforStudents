import requests

from aiogram import Router
from aiogram.filters.text import Text
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton

from bots.keybords.kb import data_confirmation, registration, menu

router = Router()


class Register(StatesGroup):
    group_selection = State()
    input_name = State()
    input_surname = State()
    last_step = State()


registration_data = {}


@router.message(Text(text='Регистрация'))
async def choice_group(message: Message, state: FSMContext):
    response = requests.get('http://localhost:8000/api/v1/get_groups')
    builder = InlineKeyboardBuilder()
    for group in response.json():
        builder.row(
            InlineKeyboardButton(
                text=group['group_number'],
                callback_data=f'group {group["group_number"]}'
            )
        )
    await message.answer('В какой ты группе?', reply_markup=builder.as_markup())
    await state.set_state(Register.group_selection)


@router.callback_query(Register.group_selection, Text(startswith='group'))
async def input_name(callback: CallbackQuery, state: FSMContext):
    data = callback.data.split(' ')
    registration_data[callback.from_user.id] = {'group_number': data[1],
                                                'name': '',
                                                'surname': ''}
    await callback.message.answer('Как тебя зовут? (отправь своё имя)')
    await state.set_state(Register.input_name)


@router.message(Register.input_name, Text)
async def input_surname(message: Message, state: FSMContext):
    data = message.text
    registration_data[message.from_user.id]['name'] = data
    await message.answer('Отправь свою фамилию')
    await state.set_state(Register.input_surname)


@router.message(Register.input_surname, Text)
async def get_name_surname(message: Message, state: FSMContext):
    data = message.text
    registration_data[message.from_user.id]['surname'] = data
    await message.answer(
        f'Твоя группа {registration_data[message.from_user.id]["group_number"]}. '
        f'Зовут тебя {registration_data[message.from_user.id]["name"]} '
        f'{registration_data[message.from_user.id]["surname"]}. Верно?', reply_markup=data_confirmation)
    await state.set_state(Register.last_step)


@router.message(Register.last_step, Text(text='Нет, не так'))
async def wrong_registration(message: Message, state: FSMContext):
    await message.answer('Начнём регистрацию снова', reply_markup=registration)
    await state.set_state(Register.group_selection)


@router.message(Register.last_step, Text(text='Да, именно так'))
async def finish_registration(message: Message, state: FSMContext):
    payload = {
        'name': registration_data[message.from_user.id]['name'],
        'surname': registration_data[message.from_user.id]['surname'],
        'group_number': {'group_number': registration_data[message.from_user.id]['group_number']},
        'telegram_id': message.from_user.id
    }
    response = requests.post('http://localhost:8000/api/v1/add_profile', json=payload)
    if response.status_code in (200, 201):
        await message.answer('Регистрация успешно пройдена', reply_markup=menu)
        await state.clear()
    else:
        await message.answer('Что-то пошло не так. Начнём регистрацию с начала', reply_markup=registration)
        await state.set_state(Register.group_selection)
