import os

from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse
from django.core.validators import (MaxValueValidator,
                                    MinValueValidator,
                                    ValidationError)
from ckeditor.fields import RichTextField


class Type(models.Model):
    title = models.CharField('Название', max_length=100)
    create_dt = models.DateTimeField('Дата создания', auto_now_add=True)
    update_dt = models.DateTimeField('Дата изменения', auto_now=True)

    class Meta:
        verbose_name = 'Тип книги'
        verbose_name_plural = 'Типы книг'

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField('ФИО автора', max_length=150)
    create_dt = models.DateTimeField('Дата создания', auto_now_add=True)
    update_dt = models.DateTimeField('Дата изменения', auto_now=True)

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def __str__(self):
        return self.name


class Tag(models.Model):
    title = models.CharField('Название', max_length=100)
    slug = models.SlugField('ЧПУ', max_length=100, unique=True)
    create_dt = models.DateTimeField('Дата создания', auto_now_add=True)
    update_dt = models.DateTimeField('Дата изменения', auto_now=True)

    def get_absolute_url(self):
        return reverse('tag_item', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.title


def validate_image(self):
    valid_format = ('.dox',)
    ext = os.path.splitext(self.image)[1]
    if not ext.lower() in valid_format:
        raise ValidationError(u'Unsupported file extension.')


class Book(models.Model):
    array_language = {
        (1, 'Русский'),
        (2, 'Английский'),
    }
    array_status = {
        (1, 'Опубликовано'),
        (2, 'На модерации'),
        (3, 'Заблокированно')
    }
    title = models.CharField('Название', max_length=100)
    user = models.ForeignKey(User,
                             verbose_name='Пользователь',
                             on_delete=models.SET_NULL,
                             null=True)
    type_id = models.ForeignKey(Type,
                                verbose_name='Тип литературы',
                                on_delete=models.SET_NULL,
                                null=True)
    status = models.PositiveSmallIntegerField('Статус', choices=array_status, default=2)
    author = models.ManyToManyField(Author, verbose_name='Автор', blank=True)
    image = models.ImageField('Изображение', upload_to='books/images', blank=True)
    file = models.FileField('Файл', upload_to='books/files')
    link = models.CharField('Ссылка/источник', max_length=400, blank=True)
    desc = RichTextField('Описание', max_length=50000)
    language = models.PositiveSmallIntegerField('Язык', choices=array_language)
    pages = models.PositiveSmallIntegerField('Колличество страниц', validators=[
        MinValueValidator(1),
        MaxValueValidator(5000)
    ])
    year = models.PositiveSmallIntegerField('Год выпуска', validators=[
        MinValueValidator(1800),
        MaxValueValidator(2150)
    ])
    tags = models.ManyToManyField(Tag, verbose_name='Теги', blank=True, related_name='books')
    create_dt = models.DateTimeField('Дата создания', auto_now_add=True)
    update_dt = models.DateTimeField('Дата изменения', auto_now=True)

    def get_absolute_url(self):
        return reverse('book_item', kwargs={'pk': self.id})

    def get_status_book(self):
        for item in self.array_status:
            if item[0] == self.status:
                return item[1]
        return '-'

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return self.title


class Article(models.Model):
    array_status = {
        (1, 'Опубликовано'),
        (2, 'На модерации'),
        (3, 'Заблокированно')
    }
    title = models.CharField('Название', max_length=100, db_index=True)
    slug = models.SlugField('ЧПУ', max_length=150, unique=True)
    user = models.ForeignKey(User,
                             verbose_name='Пользователь',
                             on_delete=models.SET_NULL,
                             null=True)
    type_id = models.ForeignKey(Type,
                                verbose_name='Тип литературы',
                                on_delete=models.SET_NULL,
                                null=True)
    status = models.PositiveSmallIntegerField('Статус', choices=array_status)
    desc = models.TextField('Описание', max_length=50000)
    link = models.CharField('Ссылка', max_length=400)
    tags = models.ManyToManyField(Tag, verbose_name='Теги', blank=True, related_name='articles')
    create_dt = models.DateTimeField('Дата создания', auto_now_add=True)
    update_dt = models.DateTimeField('Дата изменения', auto_now=True)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title
