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
    # Обновление данных по конкретному клиенту
    path('update_client/<int:client_id>/', views.update_client, name='update_client'),

    # Страница со списком всех контрагентов
    path('contractors/', views.contractors, name='contractors'),
    # Страница с подробной информацией по отдельному контрагенту, показывает все связанные грузы
    path('contractors/<int:contractor_id>/', views.contractor, name='contractor'),
    # Страница для добавления нового контрагента
    path('new_contractor/', views.new_contractor, name='new_contractor'),
    # Обновление данных по конкретному контрагенту
    path('update_contractor/<int:contractor_id>/', views.update_contractor, name='update_contractor'),

    # Страница со списком всех пользователей
    path('customers/', views.customers, name='customers'),
    # Страница с подробной информацией по отдельному пользователю, показывает все связанные грузы
    path('customers/<int:customer_id>/', views.customer, name='customer'),
    # Страница для добавления нового пользователя
    path('new_customer/', views.new_customer, name='new_customer'),
    # Обновление данных по конкретному контрагенту
    path('update_customer/<int:customer_id>/', views.update_customer, name='update_customer'),

    # Страница со списком всех складов
    path('storages/', views.storages, name='storages'),
    # Страница с подробной информацией по отдельному складу, показывает все связанные грузы
    path('storages/<int:storage_id>/', views.storage, name='storage'),
    # Страница для добавления нового склада
    path('new_storage/', views.new_storage, name='new_storage'),
    # Обновление данных по конкретному складу
    path('update_storage/<int:storage_id>/', views.update_storage, name='update_storage'),

    # Страница со списком всех грузов
    path('atms/', views.atms, name='atms'),
    # Страница с подробной информацией по отдельному грузу, показывает все связанные заявки
    path('atms/<int:atm_id>/', views.atm, name='atm'),
    # Страница для добавления нового груза
    path('new_atm/', views.new_atm, name='new_atm'),
    # Обновление данных по конкретному грузу
    path('update_atm/<int:atm_id>/', views.update_atm, name='update_atm'),

    # Страница со списком всех заявок от клиента
    path('orders/', views.orders, name='orders'),
    # Страница для добавления новой заявки
    path('new_order/', views.new_order, name='new_order'),
    # Обновление данных по конкретной заявке
    path('update_order/<int:order_id>/', views.update_order, name='update_order'),

    # Страница со списком всех операций
    path('operations/', views.operations, name='operations'),
    # Страница для добавления новой операции
    path('new_operation/', views.new_operation, name='new_operation'),
]