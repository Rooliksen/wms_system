# Определяет схемы URL для WMS

from django.urls import path

from . import views

app_name = 'wms'
urlpatterns = [
    # Домашняя страница
    path('', views.index, name='index'),
    # Страница со списком всех клиентов
    path('clients/', views.clients, name='clients'),
    # Страница с подробной информацией по отдельному клиенту, показывает все грузы клиента
    path('clients/<int:client_id>/', views.client, name='client'),
    # Страница для добавления нового клиента
    path('new_client/', views.new_client, name='new_client'),

    # Страница со списком всех контрагентов
    path('contractors/', views.contractors, name='contractors'),
    # Страница с подробной информацией по отдельному контрагенту, показывает все связанные грузы
    path('contractors/<int:contractor_id>/', views.contractor, name='contractor'),
    # Страница для добавления нового контрагента
    path('new_contractor/', views.new_contractor, name='new_contractor'),

    # Страница со списком всех пользователей
    path('customers/', views.customers, name='customers'),
    # Страница с подробной информацией по отдельному контрагенту, показывает все связанные грузы
    path('customers/<int:customer_id>/', views.customer, name='customer'),
    # Страница для добавления нового пользователя
    path('new_customer/', views.new_customer, name='new_customer'),

    # Страница со списком всех складов
    path('storages/', views.storages, name='storages'),
    # Страница с подробной информацией по отдельному складу, показывает все связанные грузы
    path('storages/<int:storage_id>/', views.storage, name='storage'),
    # Страница для добавления нового пользователя
    path('new_storage/', views.new_storage, name='new_storage'),

    # Страница со списком всех грузов
    path('atms/', views.atms, name='atms'),
    # Страница для добавления нового пользователя
    path('new_atm/', views.new_atm, name='new_atm'),

    # Страница со списком всех заявок от клиента
    path('orders/', views.orders, name='orders'),
]