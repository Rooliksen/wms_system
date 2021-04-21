# Определяет схемы URL для пользователей

from django.urls import path, include
from django.contrib.auth import views
from .views import *

from .forms import UserLoginForm

app_name = 'users'
urlpatterns = [
    # Включить URL авторизации по умолчанию.
    path('', include('django.contrib.auth.urls')),
    # Страница регистрации.
	path('register/', registerPage, name="register"),
    path('logout/', logoutUser, name="logoutUser"),
	path('login/', views.LoginView.as_view(
            template_name="login.html",
            authentication_form=UserLoginForm
            ), name="login"),
]
