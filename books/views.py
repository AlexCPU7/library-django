from django.shortcuts import render, get_object_or_404
from django.views.generic import View

from .models import Book, Tag
from .utils import ObjectItemMixin


class BookCatalog(View):
    def get(self, request):
        books = Book.objects.filter(status=1)
        return render(request, 'books/books_list.html', {
            'books': books,
        })


class BookItem(View):
    def get(self, request, pk):
        book = get_object_or_404(Book, id=pk)
        return render(request, 'books/book_item.html', {
            'book': book,
        })


class TagsList(View):
    def get(self, request):
        tags = Tag.objects.all()
        return render(request, 'books/tags_list.html', {
            'tags': tags
        })


class TagItem(ObjectItemMixin, View):
    model = Tag
    template = 'books/tag_item.html'

