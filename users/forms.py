from django.forms import ModelForm

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.validators import UnicodeUsernameValidator

class CreateUserForm(UserCreationForm):

	error_messages = {
		'password_mismatch': ("Введенные пароли не совпадают. Попробуйте ввести еще раз."),
		'unique': 'Пользователь с таким логином уже существует',
		'invalid': 'Некорректный логин. Допускается использование только букв, цифр и символов @/./+/-/_',
		}

	password1 = forms.CharField(
		label=("Пароль"),
		help_text=("Должен состоять из латинских букв и цифр, также содержать не менее 8 символов. Не может состоять только из цифр. Пример Q123456q"),
		widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control', 'placeholder': 'Придумайте пароль'}),
	)
	password2 = forms.CharField(
		label=("Пароль еще раз"),
		widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control', 'placeholder': 'Повторите пароль'}),
	)
	username = forms.CharField(
		label=("Имя аккаунта"),
		widget=forms.TextInput(attrs={'autocomplete': 'new-password', 'class': 'form-control', 'placeholder': 'Придумайте логин'}),
		error_messages={'unique': 'Пользователь с таким именем уже существует. Придумайте другой логин.',}
	)

	email = forms.CharField(
		label=("E-mail"),
		widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Введите почтовый ящик'}),
		error_messages={'unique': 'Пользователь с таким почтовым ящиком уже существует', 'invalid': 'Некорректный адрес почты.'}
		
	)

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']
		help_texts = {
			'username': 'Допускается использование букв, цифр и символов @/./+/-/_',
			'email': 'Формат адреса example@email.ru',
		}

class CustomUsernameField(UsernameField):
    def to_python(self, value):
        return unicodedata.normalize('NFKC', super().to_python(value))

    def widget_attrs(self, widget):
        return {
            **super().widget_attrs(widget),
            'autocapitalize': 'none',
            'autocomplete': 'username',
			'class': 'form-control',
        }

class UserLoginForm(AuthenticationForm):
    username = CustomUsernameField(widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control'}))
    password = forms.CharField(
        label=("Пароль"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class': 'form-control'}),
    )

    error_messages = {
        'invalid_login': (
            "Некорректные логин или пароль. Проверьте введенные "
            "данные еще раз и повторите вход."
        ),
    }