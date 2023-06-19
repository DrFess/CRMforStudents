import requests

from aiogram import Router
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, PollAnswer

from bots.keybords.kb import start_final_test, next2_question, test_result, menu

router = Router()


class TotalTesting(StatesGroup):
    start = State()
    poll = State()
    question = State()
    finish = State()


@router.message(Text(text='Итоговый тест за 1й семестр'))
async def start_test(message: Message, state: FSMContext):
    await state.set_state(TotalTesting.start)
    response = requests.get('http://localhost:8000/api/v1/test/all')
    questions = response.json()

    await state.update_data(
        student_id=message.from_user.id,
        date=message.date.today().strftime('%Y-%m-%d'),
        questions=questions,
        count=0
    )
    await message.answer('Тест загружен. Начать тест?', reply_markup=start_final_test)


@router.message(TotalTesting.start, Text(text=['Начать тест', 'Следующий вопрос']))
async def ask_question(message: Message, state: FSMContext):
    data = await state.get_data()

    if data['count'] <= (len(data['questions']) - 1):
        serial_number = data['count']

        question = data['questions']

        question_text = question[serial_number]['text']
        options = [
            question[serial_number]['answer_1'],
            question[serial_number]['answer_2'],
            question[serial_number]['answer_3'],
            question[serial_number]['answer_4']
        ]
        await message.answer_poll(
            question=question_text,
            options=options,
            is_anonymous=False,
            reply_markup=next2_question
        )

        await state.update_data(
            theme_id=question[serial_number]['theme_id'],
            correct_answer=question[serial_number]['correct_answer'],
            text=question_text,
            count=data['count'] + 1
        )

        await state.set_state(TotalTesting.question)

    else:
        await message.answer('Вопросы по теме закончились', reply_markup=test_result)
        await state.set_state(TotalTesting.finish)


@router.poll_answer(TotalTesting.question)
async def answer_poll(answer: PollAnswer, state: FSMContext):
    await state.update_data(student_answer=answer.option_ids[0] + 1)
    info = await state.get_data()
    data = {
        'total_student_id': info['student_id'],
        'total_date': info['date'],
        'total_theme': info['theme_id'],
        'total_correct_answer': info['correct_answer'],
        'total_student_answer': info['student_answer'],
        'total_text': info['text'],
    }
    requests.post('http://localhost:8000/api/v1/total_student_answers', json=data)
    await state.set_state(TotalTesting.start)


@router.message(TotalTesting.finish, Text(text='Покажи результат'))
async def total(message: Message, state: FSMContext):
    state_data = await state.get_data()
    data = {
        'total_student_id': state_data['student_id'],
        'total_date': state_data['date'],
    }
    response = requests.get('http://localhost:8000/api/v1/total_student_answers', json=data)
    result = response.json()['result']
    if result > 100:
        await message.answer('Что-то пошло не так. Обратись к преподавателю')
    else:
        await message.answer(f'Правильных ответов {result}%', reply_markup=menu)
    await state.clear()
