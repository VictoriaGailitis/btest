# Generated by Django 5.2.2 on 2025-06-09 07:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_full_name', models.CharField(max_length=255, verbose_name='ФИО')),
                ('student_group', models.CharField(max_length=100, verbose_name='Группа')),
                ('total_score', models.FloatField(verbose_name='Набрано баллов')),
                ('max_score', models.FloatField(verbose_name='Максимум баллов')),
                ('percent', models.FloatField(help_text='Процент правильных ответов', verbose_name='Процент')),
                ('started_at', models.DateTimeField(verbose_name='Начало теста')),
                ('finished_at', models.DateTimeField(verbose_name='Окончание теста')),
                ('duration_sec', models.IntegerField(verbose_name='Время прохождения (сек)')),
                ('details', models.JSONField(verbose_name='Детальные ответы')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='results', to='quiz.test', verbose_name='Тест')),
            ],
            options={
                'verbose_name': 'Результат теста',
                'verbose_name_plural': 'Результаты тестов',
                'ordering': ['-created_at'],
            },
        ),
    ]
