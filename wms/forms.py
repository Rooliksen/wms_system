from django import forms


from .models import *

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name']
        labels = {'name': 'Наименование'}
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control col-12'}),
        }

class ContractorForm(forms.ModelForm):
    class Meta:
        model = Contractor
        fields = ['name']
        labels = {'name': 'Наименование'}
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control col-12'}),
        }

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
        widgets = {
            'user': forms.Select(attrs={'class': 'form-select col-12'}),
            'name': forms.TextInput(attrs={'class': 'form-control col-12'}),
            'post': forms.TextInput(attrs={'class': 'form-control col-12'}),
            'phone': forms.TextInput(attrs={'class': 'form-control col-12'}),
            'email': forms.EmailInput(attrs={'class': 'form-control col-12'})
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
        widgets = {
            'contractor': forms.Select(attrs={'class': 'form-select col-12'}),
            'address': forms.TextInput(attrs={'class': 'form-control col-12'}),
            'rate_pallet': forms.TextInput(attrs={'class': 'form-control col-12'}),
            'rate_oversize_pallet': forms.TextInput(attrs={'class': 'form-control col-12'}),
            'rate_volume': forms.TextInput(attrs={'class': 'form-control col-12'}),
            'rate_in': forms.TextInput(attrs={'class': 'form-control col-12'}),
            'rate_out': forms.TextInput(attrs={'class': 'form-control col-12'}),
            'rate_oversize_in': forms.TextInput(attrs={'class': 'form-control col-12'}),
            'rate_oversize_out': forms.TextInput(attrs={'class': 'form-control col-12'}),
            }



class AtmForm(forms.ModelForm):
    class Meta:
        model = Atm
        fields = [
            'status',
            'client',
            'storage',
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
            'name': 'Наименование',
            'serial_num': 'Серийный номер',
            'atm_id': 'ID груза',
            'size': 'Размер',
            'commentary': 'Комментарий',
            }
        widgets = {
            'status': forms.Select(attrs={'class': 'form-select col-12'}),
            'client': forms.Select(attrs={'class': 'form-select col-12'}),
            'storage': forms.Select(attrs={'class': 'form-select col-12'}),
            'name': forms.TextInput(attrs={'class': 'form-control col-12'}),
            'serial_num': forms.TextInput(attrs={'class': 'form-control col-12'}),
            'atm_id': forms.TextInput(attrs={'class': 'form-control col-12'}),
            'size': forms.Select(attrs={'class': 'form-select col-12'}),
            'commentary': forms.TextInput(attrs={'class': 'form-control col-12'}),
            }
        

class OrderForm(forms.ModelForm):
    date_in = forms.TextInput()
    date_out = forms.TextInput()
    class Meta:
        model = Order
        fields = [
            'logistic_order',
            'client',
            'storage',
            'status',
            'date_in',
            'date_out',
            'driver',
            'driver_car',
            'storage_order',
            ]
        labels = {
            'logistic_order': 'Номер заявки клиента',
            'client': 'Клиент',
            'storage': 'Склад',
            'status': 'Статус',
            'date_in': 'Дата приема',
            'date_out': 'Дата отгрузки',
            'driver': 'ФИО водителя',
            'driver_car': 'Марка и госномер авто',
            'storage_order': 'Номер заявки склада',
            }
        widgets = {
            'logistic_order': forms.TextInput(attrs={'class': 'form-control col-12'}),
            'client': forms.Select(attrs={'class': 'form-select col-12'}),
            'storage': forms.Select(attrs={'class': 'form-select col-12'}),
            'status': forms.Select(attrs={'class': 'form-select col-12'}),
            'date_in': forms.DateInput(attrs={'class': 'form-control col-12'}),
            'date_out': forms.DateInput(attrs={'class': 'form-control col-12'}),
            'driver': forms.TextInput(attrs={'class': 'form-control col-12'}),
            'driver_car': forms.TextInput(attrs={'class': 'form-control col-12'}),
            'storage_order': forms.TextInput(attrs={'class': 'form-control col-12'}),
            }

class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = []
        labels = {'name': 'Наименование', 'order': 'Заявка'}
            