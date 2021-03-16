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

class OperationForm(forms.ModelForm):
    class Meta:
        model = Operation
        fields = ['contractor', 'name', 'cost_client', 'cost_contractor']
        labels = {
            'contractor': 'Контрагент',
            'name': 'Наименование операции',
            'cost_client': 'Стоимость',
            'cost_contractor': 'Себестоимость',
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
    date_in = forms.DateField(
        required=False,
        input_formats=['%d.%m.%Y','%d/%m/%Y'],
        label="Дата приема")
    date_out = forms.DateField(
        required=False,
        input_formats=['%d.%m.%Y','%d/%m/%Y'],
        label="Дата отгрузки")
    class Meta:
        model = Atm
        fields = [
            'orders',
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
            'orders': 'Заявки',
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

class OrderForm(forms.ModelForm):
    date_in = forms.DateField(
        required=False,
        input_formats=['%d.%m.%Y','%d/%m/%Y'],
        label="Дата приема")
    date_out = forms.DateField(
        required=False,
        input_formats=['%d.%m.%Y','%d/%m/%Y'],
        label="Дата отгрузки")
    class Meta:
        model = Order
        fields = [
            'logistic_order',
            'client',
            'customer',
            'storage',
            'status',
            'date_in',
            'date_out',
            'operation',
            'driver',
            'driver_car',
            'storage_order',
            ]
        labels = {
            'logistic_order': 'Номер заявки клиента',
            'client': 'Клиент',
            'customer': 'Пользователь',
            'storage': 'Склад',
            'status': 'Статус',
            'date_in': 'Дата приема',
            'date_out': 'Дата отгрузки',
            'operation': 'Вид операции',
            'driver': 'ФИО водителя',
            'driver_car': 'Марка и госномер авто',
            'storage_order': 'Номер заявки склада',
            }
            