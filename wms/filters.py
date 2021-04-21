import django_filters
from django_filters import DateFilter, CharFilter
from django import forms

from .models import *

class AtmFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="date_in", lookup_expr='gte')
    end_date = DateFilter(field_name="date_out", lookup_expr='lte')
    serial_num = CharFilter(field_name='serial_num', lookup_expr='icontains', widget=forms.TextInput(attrs={
        'placeholder': 'Поиск по s/n',
        'class': 'form-control',
        'aria-label': 'Example text with button addon',
        'aria-describedby': 'button-addon1'}))
    name = CharFilter(field_name='name', lookup_expr='icontains')
    storage = CharFilter(field_name='storage__address', lookup_expr='icontains', widget=forms.TextInput(attrs={
        'type': 'text',
        'placeholder': 'Поиск по складу',
        'class': 'form-control',
        'aria-label': 'Example text with button addon',
        'aria-describedby': 'button-addon1'}))
    
    class Meta:
        model = Atm
        fields = ['status', 'client', 'name', 'storage']
        filter_overrides = {
            models.ImageField: {
                'filter_class': django_filters.CharFilter,
                'extra': lambda f: {
                    'lookup_expr': 'icontains',
                },
            },
        }