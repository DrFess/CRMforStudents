# Generated by Django 4.2 on 2023-06-11 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_remove_group_subgroup_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='date_of_birth',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='phone_number',
        ),
    ]
