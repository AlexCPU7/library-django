from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, TemplateView, CreateView
from django.views.generic.list import ListView
from django.db.models import Q
from django.http import HttpResponse, HttpResponseNotFound
from django.contrib.auth.models import User

from .models import Book, Tag
from .utils import ObjectItemMixin
from .forms import CreateBookForm


class BookCatalog(View):
    def get(self, request):
        books = Book.objects.filter(status=1)
        return render(request, 'books/books_list.html', {
            'books': books,
        })


class BookItem(View):
    def get(self, request, pk):
        book = get_object_or_404(Book, (Q(id=pk, user=1) | Q(id=pk, status=1)))
        # (user=user_id) OR (status = 1)
        return render(request, 'books/book_item.html', {
            'book': book,
        })


class TagsList(View):
    def get(self, request):
        tags = Tag.objects.all()
        return render(request, 'books/tags_list.html', {
            'tags': tags
        })


class CreateBook(CreateView):
    model = Book
    form_class = CreateBookForm
    template_name = 'books/create_book.html'

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('books_list')
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(CreateBook, self).get_context_data(**kwargs)
        context['title'] = 'Добавить книгу'
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        post = form.save()
        return redirect('book_item', pk=post.id)


class MyBook(View):
    template_name = 'books/my_book.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            books = Book.objects.filter(user=self.request.user)
            return render(request, self.template_name, {'books': books,
                                                        'title': 'Мои книги'})
        else:
            return redirect('books_list')


class TagItem(ObjectItemMixin, View):
    model = Tag
    template = 'books/tag_item.html'

