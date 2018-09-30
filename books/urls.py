from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_catalog, name='catalog'),
    path('book/<int:id>', views.book_item, name='item'),
]
