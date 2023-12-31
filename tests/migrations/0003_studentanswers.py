# Generated by Django 4.2 on 2023-06-16 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0002_alter_category_options_alter_question_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentAnswers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.IntegerField(verbose_name='ID телеграм аккаунта')),
                ('theme', models.CharField(verbose_name='Тема теста(число)')),
                ('correct_answer', models.IntegerField(verbose_name='Правильный ответ')),
                ('student_answer', models.IntegerField(verbose_name='Ответ студента')),
                ('date', models.DateField(verbose_name='Дата ответа')),
            ],
            options={
                'verbose_name': 'Ответ студента',
                'verbose_name_plural': 'Ответы студента',
                'ordering': ['student_id', 'theme', 'date'],
            },
        ),
    ]
