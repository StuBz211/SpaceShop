"""
Модуль для хранения примесей моделей.
смысл такой, выделить повторяющиеся поля для модели,
и вынести их в отдельные абстрактные классы
"""
from django.db import models


class TitleMixin(models.Model):
    class Meta:
        abstract = True

    title = models.CharField(max_length=100)


class DescriptionMixin(models.Model):
    class Meta:
        abstract = True

    description = models.TextField()
