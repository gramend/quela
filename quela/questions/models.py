from django.db import models
from django.conf import settings


class Category(models.Model):

    categories = models.ManyToManyField(
        "Category",
        verbose_name="Категория",
        blank=True,
    )
    name = models.CharField(verbose_name="Название Тега/Категории:", max_length=255)
    comment = models.TextField(
        verbose_name="Описание Тега/Категории",
        blank=True,
    )
    assigned_groups = models.ManyToManyField(
        "auth.Group",
        verbose_name="Группа студентов",
        blank=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Question(models.Model):

    OPEN_QUESTION = "OPQ"
    CHOICES_QUESTION = "CHQ"
    MULTI_CHOICES_QUESTION = "MCQ"
    ORDER_QUESTION = "ORQ"
    MATCH_QUESTION = "MCH"
    QUESTION_TYPES = [
        (OPEN_QUESTION, "Открытый вопрос"),
        (CHOICES_QUESTION, "Вопрос с выбором ответа"),
        (MULTI_CHOICES_QUESTION, "Вопрос с выбором нескольких ответов"),
        (ORDER_QUESTION, "Вопрос на расстановку в правильной последовательности"),
        (MATCH_QUESTION, "Вопрос на соответствие"),
    ]

    LIGHT_LVL = "LLVL"
    MIDDLE_LVL = "MLVL"
    HIGH_LVL = "HLVL"
    QUESTION_LEVELS = [
        (LIGHT_LVL, "Вопрос на определения"),
        (MIDDLE_LVL, "Вопрос на понимание определения"),
        (HIGH_LVL, "Решение практических задач"),
    ]

    text = models.TextField(verbose_name="Описание вопроса")
    questionType = models.CharField(
        verbose_name="Тип вопроса",
        max_length=3,
        choices=QUESTION_TYPES,
    )
    questionLevel = models.CharField(
        verbose_name="Уровень вопроса",
        max_length=4,
        choices=QUESTION_LEVELS,
    )
    categories = models.ManyToManyField(
        "Category",
        verbose_name="Категория",
        blank=True,
        )

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"


class Answer(models.Model):
    question = models.ForeignKey(
        Question,
        verbose_name="Вопрос",
        on_delete=models.PROTECT
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        verbose_name='Студент',
    )
    text = models.TextField(verbose_name="Текст ответа")
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Ответ"
        verbose_name_plural = "Ответы"


class Comment(models.Model):
    answer = models.ForeignKey(
        Answer,
        verbose_name="Комментарий",
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        verbose_name="Пользователь"
    )
    text = models.TextField(verbose_name="Текст комментария:")
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
