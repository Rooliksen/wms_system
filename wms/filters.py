import django_filters
from django_filters import DateFilter, CharFilter

from .models import *

class AtmFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="date_in", lookup_expr='gte')
    end_date = DateFilter(field_name="date_out", lookup_expr='lte')
    serial_num = CharFilter(field_name='serial_num', lookup_expr='icontains')
    name = CharFilter(field_name='name', lookup_expr='icontains')
    
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