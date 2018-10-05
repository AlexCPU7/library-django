from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_catalog, name='books_list'),
    path('book/<int:pk>', views.book_item, name='book_item'),
    path('tags/', views.tags_list, name='tags_list'),
    path('tag/<str:slug>', views.tag_item, name='tag_item')
]
