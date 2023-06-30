from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

menu_items_for_teacher = [
    [KeyboardButton(text='Геопозиция'),
     KeyboardButton(text='Получить результат тестирования')],
]

menu_for_teacher = ReplyKeyboardMarkup(keyboard=menu_items_for_teacher, one_time_keyboard=True, resize_keyboard=True)

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

yes_or_no_button = [KeyboardButton(text='Да'), KeyboardButton(text='Нет')]
yes_or_no = ReplyKeyboardMarkup(keyboard=[yes_or_no_button], one_time_keyboard=True, resize_keyboard=True)

date_or_not_date_button = [KeyboardButton(text='По дате'), KeyboardButton(text='Без даты')]
date_or_not_date = ReplyKeyboardMarkup(keyboard=[date_or_not_date_button], one_time_keyboard=True, resize_keyboard=True)

show_calendar_button = [KeyboardButton(text='Покажи')]
show_calendar = ReplyKeyboardMarkup(keyboard=[show_calendar_button], one_time_keyboard=True, resize_keyboard=True)

show_answers_button = [KeyboardButton(text='Покажи')]
show_answers = ReplyKeyboardMarkup(keyboard=[show_answers_button], one_time_keyboard=True, resize_keyboard=True)