# Определяет схемы URL для WMS

from django.urls import path

from . import views

app_name = 'wms'
urlpatterns = [
    # Домашняя страница
    path('', views.index, name='index'),
    # Страница со списком всех клиентов
    path('clients/', views.clients, name='clients'),
    # Страница со списком всех контрагентов
    path('contractors/', views.contractors, name='contractors'),
    # Страница со списком всех пользователей
    path('customers/', views.customers, name='customers'),
    # Страница со списком всех складов
    path('storages/', views.storages, name='storages'),
]