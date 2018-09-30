from django.shortcuts import render, get_object_or_404
from .models import Book


def book_catalog(request):
    books = Book.objects.filter(status=1)
    return render(request, 'books/book_catalog.html', {
            'books': books,
    })


def book_item(request, id):
    book = get_object_or_404(Book, id=id)
    t = [1, 2, 3]
    return render(request, 'books/book_item.html', {
        'book': book,
        't': t
    })

