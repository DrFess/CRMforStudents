def calculate_result(answers: dict, length: int, student: str, correct: str) -> int:
    count = 0
    for item in answers.values():
        if item[f'{student}'] == item[f'{correct}']:
            count += 1
    test_result = round((count / length) * 100)
    return test_result
