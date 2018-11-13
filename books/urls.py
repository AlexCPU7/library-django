from django.urls import path
from . import views

urlpatterns = [
    path('', views.BookCatalog.as_view(), name='books_list'),
    path('my-book/', views.MyBook.as_view(), name='my_book_url'),
    path('book/create-book', views.CreateBook.as_view(), name='create_book_url'),
    path('book/<int:pk>', views.BookItem.as_view(), name='book_item'),
    path('tags/', views.TagsList.as_view(), name='tags_list'),
    path('tag/<str:slug>', views.TagItem.as_view(), name='tag_item')
]
