from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='info_index'),
    path('registration/', views.Registration.as_view(), name='registration_url'),
    path('login/', views.Login.as_view(), name='login_url'),
    path('logout/', views.Logout.as_view(), name='logout_url')
]
