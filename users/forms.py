from django.forms import ModelForm

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.validators import UnicodeUsernameValidator

class CreateUserForm(UserCreationForm):
	password1 = forms.CharField(
		label=("Пароль"),
		help_text=("Должен содержать не менее 8 символов, не может состоять только из цифр."),
		widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control col-sm-3', 'placeholder': 'Придумайте пароль'}),
	)
	password2 = forms.CharField(
		label=("Пароль еще раз"),
		widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control col-sm-3', 'placeholder': 'Повторите пароль'}),
	)
	username = forms.CharField(
		label=("Имя аккаунта"),
		widget=forms.TextInput(attrs={'autocomplete': 'new-password', 'class': 'form-control col-sm-3', 'placeholder': 'Придумайте логин'}),
		error_messages={'unique': 'Пользователь с таким логином уже существует', 'invalid': 'Некорректный логин. Допускается использование только букв, цифр и символов @/./+/-/_'}
		
	)

	email = forms.CharField(
		label=("E-mail"),
		widget=forms.EmailInput(attrs={'class': 'form-control col-sm-3', 'placeholder': 'Введите почтовый ящик'}),
		error_messages={'unique': 'Пользователь с таким почтовым ящиком уже существует', 'invalid': 'Некорректный адрес почты.'}
		
	)

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']
		help_texts = {
			'username': 'Должен содержать не менее 8 символов. Допускается использование букв, цифр и символов @/./+/-/_',
			'email': 'Формат адреса example@email.ru',
		}

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
		label=("Password"),
		widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control col-sm-3'})
	)
    password = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class': 'form-control col-sm-3'}),
    )

    error_messages = {
        'invalid_login': (
            "Please enter a correct %(username)s and password. Note that both "
            "fields may be case-sensitive."
        ),
        'inactive': ("This account is inactive."),
    }