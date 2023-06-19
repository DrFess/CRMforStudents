import requests
import pandas as pd

xlsx_file_path = "/Users/aleksejdegtarev/Desktop/Тест студентам.xlsx"

df = pd.read_excel(xlsx_file_path)

for index, row in df.iterrows():
    data = {
        'text': row['Вопросы'],
        'answer_1': row['Вариант 1'],
        'answer_2': row['Вариант 2'],
        'answer_3': row['Вариант 3'],
        'answer_4': row['Вариант 4'],
        'correct_answer': row['answer'],
        'theme': {'title': row['Тема']}
    }
    try:
        response = requests.post('http://localhost:8000/api/v1/add_question', json=data)
    except Exception as e:
        print(e)
