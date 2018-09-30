from django.contrib import admin
from .models import Book, Article, Type, Author, Tag


admin.site.register(Book)
admin.site.register(Article)
admin.site.register(Type)
admin.site.register(Author)
admin.site.register(Tag)
