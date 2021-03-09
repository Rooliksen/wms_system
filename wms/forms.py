from django import forms

from .models import *

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name']
        labels = {'name': 'Наименование'}

class ContractorForm(forms.ModelForm):
    class Meta:
        model = Contractor
        fields = ['name']
        labels = {'name': 'Наименование'}

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['user', 'name', 'post', 'phone', 'email']
        labels = {
            'user': 'Логин пользователя',
            'name': 'Имя',
            'post': 'Должность',
            'phone': 'Телефон',
            'email': 'Email',
            }

class StorageForm(forms.ModelForm):
    class Meta:
        model = Storage
        fields = [
            'contractor',
            'address',
            'rate_pallet',
            'rate_oversize_pallet',
            'rate_volume',
            'rate_in',
            'rate_out',
            'rate_oversize_in',
            'rate_oversize_out',
            ]
        labels = {
            'contractor': 'Наименование контрагента',
            'address': 'Адрес площадки',
            'rate_pallet': 'Хранение EUR, руб/сут',
            'rate_oversize_pallet': 'Хранение FIN, руб/сут',
            'rate_volume': 'Хранение V, м3/сут',
            'rate_in': 'Прием EUR, руб',
            'rate_out': 'Отгрузка EUR, руб',
            'rate_oversize_in': 'Прием FIN',
            'rate_oversize_out': 'Отгрузка FIN',
            }

class AtmForm(forms.ModelForm):
    date_in = forms.DateField(required=False, input_formats=['%d.%m.%Y','%d/%m/%Y'])
    date_out = forms.DateField(required=False, input_formats=['%d.%m.%Y','%d/%m/%Y'])
    class Meta:
        model = Atm
        fields = [
            'status',
            'client',
            'storage',
            'date_in',
            'date_out',
            'name',
            'serial_num',
            'atm_id',
            'size',
            'commentary',
            ]
        labels = {
            'status': 'Статус',
            'client': 'Клиент',
            'storage': 'Склад',
            'date_in': 'Дата приема',
            'date_out': 'Дата отгрузки',
            'name': 'Наименование',
            'serial_num': 'Серийный номер',
            'atm_id': 'ID груза',
            'size': 'Размер',
            'commentary': 'Комментарий',
            }