from django.shortcuts import render
from django.contrib.auth.models import User

from django.views.generic import View


def index(request):
    return render(request, 'info/index.html', {'title': 'Информация'})


class Registration(View):
    def get(self, request):
        return render(request, 'info/registration.html', {'title': 'Войти'})


class Login(View):
    def get(self, request):
        return render(request, 'info/login.html', {'title': 'Войти'})


class Logout(View):
    def get(self, request):
        return render(request, 'info/logout.html', {'title': 'Выйти'})
