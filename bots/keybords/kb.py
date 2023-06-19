from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

menu_items = [
    [KeyboardButton(text='Геопозиция'),
     KeyboardButton(text='Тест по теме занятия')],
    [KeyboardButton(text='Редактировать данные студента'),
     KeyboardButton(text='Помощь')],
    [KeyboardButton(text='Итоговый тест за 1й семестр')]
]

menu = ReplyKeyboardMarkup(keyboard=menu_items, one_time_keyboard=True, resize_keyboard=True)

registration_button = KeyboardButton(text='Регистрация')
registration = ReplyKeyboardMarkup(keyboard=[[registration_button]], one_time_keyboard=True, resize_keyboard=True)

truth_button = [KeyboardButton(text='Да, именно так')]
not_truth_button = [KeyboardButton(text='Нет, не так')]
data_confirmation = ReplyKeyboardMarkup(keyboard=[truth_button, not_truth_button], one_time_keyboard=True, resize_keyboard=True)

info_geolocation_button = [KeyboardButton(text='Да, подскажи')]
info_geolocation = ReplyKeyboardMarkup(keyboard=[info_geolocation_button], one_time_keyboard=True, resize_keyboard=True)

result_button = [KeyboardButton(text='Покажи результат')]
test_result = ReplyKeyboardMarkup(keyboard=[result_button], one_time_keyboard=True, resize_keyboard=True)

start_test_button = [KeyboardButton(text='Начать тест')]
start_test = ReplyKeyboardMarkup(keyboard=[start_test_button], resize_keyboard=True)

start_final_test_button = [KeyboardButton(text='Начать тест')]
start_final_test = ReplyKeyboardMarkup(keyboard=[start_test_button], resize_keyboard=True)

next_question_button = [KeyboardButton(text='Следующий вопрос')]
next_question = ReplyKeyboardMarkup(keyboard=[next_question_button], resize_keyboard=True)

next2_question_button = [KeyboardButton(text='Следующий вопрос')]
next2_question = ReplyKeyboardMarkup(keyboard=[next2_question_button], resize_keyboard=True)
