import asyncio
import logging
import requests

from aiogram import Bot, Dispatcher, Router
from aiogram.filters import Command
from aiogram.types import Message

from config import TOKEN
from bots.keybords import kb
from handlers import geolocations, test_for_students, registration, help, final_test_first_semester, edit_profile


router = Router()


@router.message(Command(commands=["start"]))
async def command_start_handler(message: Message):
    response = requests.get('http://localhost:8000/api/v1/get_field_values?data=telegram_id')
    if message.from_user.id in response.json():
        await message.answer(f"Привет, <b>{message.from_user.full_name}!</b>", reply_markup=kb.menu)
    else:
        await message.answer(f"Привет, незнакомец. Давай знакомиться", reply_markup=kb.registration)


async def main():
    bot = Bot(token=TOKEN, parse_mode="HTML")
    dp = Dispatcher()
    dp.include_routers(
        router, geolocations.router,
        test_for_students.router,
        registration.router,
        help.router,
        final_test_first_semester.router,
        edit_profile.router
    )

    # await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
