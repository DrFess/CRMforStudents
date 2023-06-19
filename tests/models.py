from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100, blank=True, verbose_name='Категория')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Question(models.Model):
    text = models.CharField(max_length=500, verbose_name='Текст вопроса')
    answer_1 = models.CharField(max_length=150, verbose_name='Вариант ответа 1')
    answer_2 = models.CharField(max_length=150, verbose_name='Вариант ответа 2')
    answer_3 = models.CharField(max_length=150, verbose_name='Вариант ответа 3')
    answer_4 = models.CharField(max_length=150, verbose_name='Вариант ответа 4')
    correct_answer = models.PositiveSmallIntegerField(verbose_name='Верный ответ')
    theme = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class StudentAnswers(models.Model):
    student_id = models.IntegerField(verbose_name='ID телеграм аккаунта')
    theme = models.CharField(verbose_name='Тема теста(число)')
    correct_answer = models.IntegerField(verbose_name='Правильный ответ')
    student_answer = models.IntegerField(verbose_name='Ответ студента')
    date = models.DateField(verbose_name='Дата ответа')
    text = models.CharField(verbose_name='Текст вопроса', blank=True)

    def __str__(self):
        return f'{self.student_id}'

    class Meta:
        verbose_name = 'Ответ студента'
        verbose_name_plural = 'Ответы студента'
        ordering = ['student_id', 'theme', 'date']


class TotalStudentAnswers(models.Model):
    total_student_id = models.IntegerField(verbose_name='ID телеграм студента')
    total_theme = models.CharField(verbose_name='Тема теста(число)')
    total_correct_answer = models.IntegerField(verbose_name='Правильный ответ')
    total_student_answer = models.IntegerField(verbose_name='Ответ студента')
    total_date = models.DateField(verbose_name='Дата ответа')
    total_text = models.CharField(verbose_name='Текст вопроса', blank=True)

    def __str__(self):
        return f'{self.total_student_id}'

    class Meta:
        verbose_name = 'Ответ студента (итоговый тест)'
        verbose_name_plural = 'Ответы студента (итоговый тест)'
        ordering = ['total_student_id', 'total_theme', 'total_date']
