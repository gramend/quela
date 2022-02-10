# Generated by Django 3.2.10 on 2021-12-16 08:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название Тега/Категории:')),
                ('comment', models.TextField(blank=True, verbose_name='Описание Тега/Категории')),
                ('assigned_groups', models.ManyToManyField(blank=True, to='auth.Group', verbose_name='Группа студентов')),
                ('categories', models.ManyToManyField(blank=True, to='questions.Category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Описание вопроса')),
                ('questionType', models.CharField(choices=[('OPQ', 'Открытый вопрос'), ('CHQ', 'Вопрос с выбором ответа'), ('MCQ', 'Вопрос с выбором нескольких ответов'), ('ORQ', 'Вопрос на расстановку в правильной последовательности'), ('MCH', 'Вопрос на соответствие')], max_length=3, verbose_name='Тип вопроса')),
                ('questionLevel', models.CharField(choices=[('LLVL', 'Вопрос на определения'), ('MLVL', 'Вопрос на понимание определения'), ('HLVL', 'Решение практических задач')], max_length=4, verbose_name='Уровень вопроса')),
                ('categories', models.ManyToManyField(blank=True, to='questions.Category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
            },
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст ответа')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='questions.question', verbose_name='Вопрос')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Студент')),
            ],
            options={
                'verbose_name': 'Ответ',
                'verbose_name_plural': 'Ответы',
            },
        ),
    ]
