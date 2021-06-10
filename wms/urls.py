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
    # Удаление конкретного груза
    path('delete_atm/<int:atm_id>/', views.delete_atm, name='delete_atm'),

    # Страница со списком всех заявок от клиента
    path('orders/', views.orders, name='orders'),
    # Страница с детальной информацией по заявке
    path('order/<int:order_id>/', views.order, name='order'),
    # Страница для просмотра фото в заявке
    path('orderphoto/<str:pk>/', views.view_orderphoto, name='orderphoto'),


    # Страница для добавления новой заявки
    path('new_order/', views.new_order, name='new_order'),
    # Обновление данных по конкретной заявке
    path('update_order/<int:order_id>/', views.update_order, name='update_order'),
    # Удаление конкретной заявки
    path('delete_order/<int:order_id>/', views.delete_order, name='delete_order'),
    # Удаление конкретного элемента заявки
    path('delete_orderitem/<int:orderitem_id>/', views.delete_orderitem, name='delete_orderitem'),
    # Удаление конкретного элемента заявки из листа на странице заявки
    path('delete_orderitem_from_list/<int:orderitem_id>/', views.delete_orderitem_from_list, name='delete_orderitem_from_list'),
    
    # Рабочая панель
    path('menu/', views.menu, name='menu'),
    # Добавление нового элемента таблицы
    path('new_order_item/<int:order_id>/<int:atm_id>/', views.new_order_item, name='new_order_item'),

    # Отправка почты
    path('emailsuccess/<int:order_id>/', views.emailsuccess, name='emailsuccess'),
]