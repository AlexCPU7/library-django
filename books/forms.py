from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from ckeditor.fields import RichTextField

from .models import Book


class CreateBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'type_id', 'image', 'file', 'link',
                  'desc', 'language', 'pages', 'year', 'tags')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'col-xl-12'}),
            'type_id': forms.Select(attrs={'class': 'col-xl-12'}),
            'author': forms.SelectMultiple(attrs={'class': 'col-xl-12'}),
            'image': forms.FileInput(attrs={'class': 'col-xl-12'}),
            'file': forms.FileInput(attrs={'class': 'col-xl-12'}),
            'link': forms.TextInput(attrs={'class': 'col-xl-12'}),
            'language': forms.Select(attrs={'class': 'col-xl-12'}),
            'pages': forms.NumberInput(attrs={'class': 'col-xl-12'}),
            'year': forms.NumberInput(attrs={'class': 'col-xl-12'}),
            'tags': forms.SelectMultiple(attrs={'class': 'col-xl-12'}),
        }
