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


class CreateBookTest(TemplateView):
    template_name = 'books/create_book.html'

    def post(self, request, *args, **kwargs):
        form = CreateBookForm(self.request.POST)
        #form.instance.user = self.request.user
        t = form.is_valid()
        if form.is_valid():
            post = form.save()
            url = post.get_url()
            return render(url)

    def get_context_data(self, **kwargs):
        context = super(CreateBookTest, self).get_context_data(**kwargs)
        context['title'] = 'Добавить Книгу'
        context['form'] = CreateBookForm()
        return context


class CreateBook(CreateView):
    model = Book
    form_class = CreateBookForm
    template_name = 'books/create_book.html'

    def get_context_data(self, **kwargs):
        context = super(CreateBook, self).get_context_data(**kwargs)
        context['title'] = 'Добавить самосвал'
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        post = form.save()
        return redirect('book_item', pk=post.id)


class MyBook(ListView):
    template_name = 'books/my_book.html'
    context_object_name = 'books'

    def get_context_data(self, request, **kwargs):
        if False:
            return HttpResponse('404')
        context = super().get_context_data(**kwargs)
        context['title'] = 'Мои книги'
        return context

    def get_queryset(self):
        try:
            if self.request.GET:
                return Book.objects.filter(user=self.request.user,
                                           model=self.request.GET['model'])
        except ValueError:
            pass
        return Book.objects.filter(user=self.request.user)


class TagItem(ObjectItemMixin, View):
    model = Tag
    template = 'books/tag_item.html'

