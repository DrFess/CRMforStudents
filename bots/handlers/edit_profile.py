from aiogram import Router
from aiogram.filters import Text
from aiogram.types import Message

from bots.keybords.kb import menu

router = Router()


@router.message(Text(text='Редактировать данные студента'))
async def start_edit(message: Message):
    await message.answer('Я пока этого не умею, только учусь', reply_markup=menu)