from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.core.validators import MaxValueValidator, MinValueValidator


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
    create_dt = models.DateTimeField('Дата создания', auto_now_add=True)
    update_dt = models.DateTimeField('Дата изменения', auto_now=True)

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.title


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
    status = models.PositiveSmallIntegerField('Статус', choices=array_status)
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
    tags = models.ManyToManyField(Tag, verbose_name='Теги', blank=True)
    create_dt = models.DateTimeField('Дата создания', auto_now_add=True)
    update_dt = models.DateTimeField('Дата изменения', auto_now=True)

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
    user = models.ForeignKey(User,
                             verbose_name='Пользователь',
                             on_delete=models.SET_NULL,
                             null=True)
    type_id = models.ForeignKey(Type,
                                verbose_name='Тип литературы',
                                on_delete=models.SET_NULL,
                                null=True)
    status = models.PositiveSmallIntegerField('Статус', choices=array_status)
    slug = models.SlugField('Слак', max_length=150, unique=True)
    desc = models.TextField('Описание', max_length=50000)
    link = models.CharField('Ссылка', max_length=400)
    tags = models.ManyToManyField(Tag, verbose_name='Теги', blank=True)
    create_dt = models.DateTimeField('Дата создания', auto_now_add=True)
    update_dt = models.DateTimeField('Дата изменения', auto_now=True)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title
