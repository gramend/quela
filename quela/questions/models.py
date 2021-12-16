from django.db import models


class Tag(models.Model):
    name = models.CharField(name="Название тега:", max_length=255)

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

    text = models.TextField(name="Описание вопроса", max_length=255)
    questionType = models.CharField(name="Тип вопроса", max_length=3, choices=QUESTION_TYPES)
    tags = models.ManyToManyField("Tag")
