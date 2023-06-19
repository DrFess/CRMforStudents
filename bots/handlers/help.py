from aiogram import Router
from aiogram.filters import Text
from aiogram.types import Message


router = Router()


@router.message(Text(text='Помощь'))
async def info(message: Message):
    await message.answer('Чтобы перезапустить бота \nнажми ---> /start.')
