from django.shortcuts import render, get_object_or_404
from .models import Book, Tag


def book_catalog(request):
    books = Book.objects.filter(status=1)
    return render(request, 'books/books_list.html', {
        'books': books,
    })


def book_item(request, pk):
    book = get_object_or_404(Book, id=pk)
    return render(request, 'books/book_item.html', {
        'book': book,
    })


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'books/tags_list.html', {
        'tags': tags
    })


def tag_item(request, slug):
    tag = Tag.objects.get(slug__iexact=slug)
    return render(request, 'books/tag_item.html', {
        'tag': tag
    })
