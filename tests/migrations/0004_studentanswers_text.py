# Generated by Django 4.2 on 2023-06-16 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0003_studentanswers'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentanswers',
            name='text',
            field=models.CharField(blank=True, verbose_name='Текст вопроса'),
        ),
    ]
