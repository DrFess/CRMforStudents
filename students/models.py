from django.db import models


class Group(models.Model):
    group_number = models.CharField(max_length=10, verbose_name='Номер группы')

    def __str__(self):
        return f'{self.group_number}'


class Profile(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    surname = models.CharField(max_length=255, verbose_name='Фамилия')
    group_number = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name='Группа и подгруппа')
    telegram_id = models.IntegerField(primary_key=True, verbose_name='ID телеграм аккаунта')

    def __str__(self):
        return f'{self.name} {self.surname}'


class Geolocation(models.Model):
    longitude = models.FloatField(verbose_name='долгота')
    latitude = models.FloatField(verbose_name='широта')
    telegram_id = models.IntegerField(verbose_name='ID телеграм аккаунта')
    date = models.DateField(verbose_name='Дата посещения')

    def __str__(self):
        return f'{self.telegram_id}'
