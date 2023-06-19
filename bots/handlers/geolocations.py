import datetime
import requests

from aiogram import Router, F
from aiogram.filters.text import Text
from aiogram.types import Message, ReplyKeyboardRemove

from bots.keybords.kb import info_geolocation


router = Router()


@router.message(Text(text='Геопозиция'))
async def send_location(message: Message):
    await message.answer(
        "Начни транслировать свою геопозицию. Если геопозицию просто отправишь - не зачту\n"
        "Подсказать как это сделать?",
        reply_markup=info_geolocation)


@router.message(Text(endswith='подскажи'))
async def how_to_share_location(message: Message):
    await message.answer_photo(
        'AgACAgIAAxkBAAKpZGSHPsxt1DBKVNzzniN7_TYMzMFVAALgyTEbA4JBSHlVtBHkEZLMAQADAgADeQADLwQ',
        caption='Нажми на "скрепку" слева от поля ввода сообщения'
    )
    await message.answer_photo(
        'AgACAgIAAxkBAAKpbmSHQCVqo6OqAn1Y-sqIzUJhmlmkAALkyTEbA4JBSPlIiYqYcYcuAQADAgADeQADLwQ',
        caption='Иногда "скрепка" может быть справа от поля ввода'
    )
    await message.answer_photo(
        'AgACAgIAAxkBAAKpcGSHQHaZ7lZbo2V0hQUvMN572RP-AALhyTEbA4JBSJJ0stNuAAHIhwEAAwIAA3kAAy8E',
        caption='В открывшемся меню внизу нажми на "Геопозиция"'
    )
    await message.answer_photo(
        'AgACAgIAAxkBAAKpcmSHQNuy4_M2GtM19MckfssJOemyAALiyTEbA4JBSP8IVhjNbvLeAQADAgADeQADLwQ',
        caption='В следующем меню выбери "Транслировать геопозицию". Длительность трансляции можно выбрать любое'
    )
    await message.answer_photo(
        'AgACAgIAAxkBAAKpdGSHQX85OJ_zd-oX5toLYymNWY8PAALjyTEbA4JBSIjJavB8yW6ZAQADAgADeQADLwQ',
        caption='Когда бот ответит что трансляцию можно остановить, нажми на "крестик" в правом верхнем углу'
    )
    await message.answer(
        'Следуя этой инструкции попробуй транслировать геопозицию\n'
        'Чтобы перезапустить бота \nнажми ---> /start.',
        reply_markup=ReplyKeyboardRemove()
    )


@router.message(F.location)
async def first_location(message: Message):
    if message.location.live_period:
        payload = {
            'longitude': message.location.longitude,
            'latitude': message.location.latitude,
            'telegram_id': message.from_user.id,
            'date': datetime.datetime.now().strftime('%Y-%m-%d')
        }
        response = requests.post('http://localhost:8000/api/v1/geolocation', json=payload)
        if response.status_code == 201:
            await message.reply("Geolocation saved successfully.")
            await message.reply("Спасибо! Теперь трансляцию можно остановить")
        else:
            await message.reply("Failed to save geolocation.")
    else:
        await message.reply("Нужно транслировать геопозицию")
