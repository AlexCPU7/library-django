from django.shortcuts import render, redirect
from django.views.generic import FormView
from django.views.generic import View
from django.contrib.auth import (login,
                                 logout)
from django.contrib.auth.forms import AuthenticationForm

from .forms import UserCreateForm


def index(request):
    return render(request, 'info/index.html', {'title': 'Информация'})


class Registration(FormView):
    template_name = 'info/registration.html'
    success_url = '/login/'
    form_class = UserCreateForm

    def form_valid(self, form):
        form.save()
        return super(Registration, self).form_valid(form)

    def form_invalid(self, form):
        return super(Registration, self).form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(Registration, self).get_context_data(**kwargs)
        context['title'] = 'Регистрация'
        return context


class Login(FormView):
    template_name = 'info/login.html'
    success_url = '/catalog'
    form_class = AuthenticationForm

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Войти'
        return context


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('login_url')
