# Generated by Django 5.1.2 on 2024-11-09 14:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Employee",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "full_name",
                    models.CharField(
                        blank=True,
                        help_text="Введите Фамилию, имя и отчество",
                        max_length=200,
                        null=True,
                        verbose_name="ФИО",
                    ),
                ),
                (
                    "position",
                    models.CharField(
                        blank=True,
                        help_text="Укажите должность работника",
                        max_length=250,
                        null=True,
                        verbose_name="Должность",
                    ),
                ),
            ],
            options={
                "verbose_name": "Сотрудник",
                "verbose_name_plural": "Сотрудники",
            },
        ),
        migrations.CreateModel(
            name="Task",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(max_length=250, verbose_name="Название задачи"),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True, null=True, verbose_name="Описание задачи"
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="Статус"
                    ),
                ),
                (
                    "time_complete",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="Дата и время выполнения"
                    ),
                ),
                (
                    "executor",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tasks",
                        to="tracker.employee",
                        verbose_name="исполнитель задачи",
                    ),
                ),
            ],
            options={
                "verbose_name": "Задача",
                "verbose_name_plural": "Задачи",
            },
        ),
    ]