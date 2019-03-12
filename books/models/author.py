import os

from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse
from django.core.validators import (MaxValueValidator,
                                    MinValueValidator,
                                    ValidationError)
from ckeditor.fields import RichTextField


class Author(models.Model):
    name = models.CharField('ФИО автора', max_length=150)
    create_dt = models.DateTimeField('Дата создания', auto_now_add=True)
    update_dt = models.DateTimeField('Дата изменения', auto_now=True)

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def __str__(self):
        return self.name
