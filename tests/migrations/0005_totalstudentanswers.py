# Generated by Django 4.2 on 2023-06-18 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0004_studentanswers_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='TotalStudentAnswers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_student_id', models.IntegerField(verbose_name='ID телеграм студента')),
                ('total_theme', models.CharField(verbose_name='Тема теста(число)')),
                ('total_correct_answer', models.IntegerField(verbose_name='Правильный ответ')),
                ('total_student_answer', models.IntegerField(verbose_name='Ответ студента')),
                ('total_date', models.DateField(verbose_name='Дата ответа')),
                ('total_text', models.CharField(blank=True, verbose_name='Текст вопроса')),
            ],
            options={
                'verbose_name': 'Ответ студента',
                'verbose_name_plural': 'Ответы студента',
                'ordering': ['total_student_id', 'total_theme', 'total_date'],
            },
        ),
    ]