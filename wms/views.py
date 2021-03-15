from django.shortcuts import render, redirect
from .models import *
from .models import Contractor
from .forms import *

def index(request):
    # Домашняя страница приложения WMS
    return render(request, 'wms/index.html')

def clients(request):
    # Выводит список клиентов
    clients = Client.objects.all().order_by('pub_date')
    context = {'clients': clients}
    return render(request, 'wms/clients.html', context)

def client(request, client_id):
    # Выводит одного клиента и все связанные с ним грузы
    client = Client.objects.get(id=client_id)
    atms = client.atm_set.order_by('-date_in')
    context = {'client': client, 'atms': atms}
    return render(request, 'wms/client.html', context)

def new_client(request):
    # Создание нового клиента
    if request.method != 'POST':
        # Данные не отправлялись; создается пустая форма.
        form = ClientForm()
    else:
        # Отправлены данные POST; обработать данные.
        form = ClientForm(data=request.POST)
        if form.is_valid():
            new_client = form.save(commit=False)
            new_client.save()
            return redirect('wms:clients')

    # Вывести пустую или недействительную форму.
    context = {'form': form}
    return render(request, 'wms/new_client.html', context)

def contractors(request):
    # Выводит список контрагентов
    contractors = Contractor.objects.all().order_by('pub_date')
    context = {'contractors': contractors}
    return render(request, 'wms/contractors.html', context)

def contractor(request, contractor_id):
    # Выводит одного контрагента и все связанные с ним грузы
    contractor = Contractor.objects.get(id=contractor_id)
    storages = Storage.objects.get(id=contractor_id)
    atms = storages.atm_set.order_by('-date_in')
    context = {'contractor': contractor, 'storages': storages, 'atms': atms}
    return render(request, 'wms/contractor.html', context)

def new_contractor(request):
    # Создание нового контрагента
    if request.method != 'POST':
        # Данные не отправлялись; создается пустая форма.
        form = ContractorForm()
    else:
        # Отправлены данные POST; обработать данные.
        form = ContractorForm(data=request.POST)
        if form.is_valid():
            new_contractor = form.save(commit=False)
            new_contractor.save()
            return redirect('wms:contractors')

    # Вывести пустую или недействительную форму.
    context = {'form': form}
    return render(request, 'wms/new_contractor.html', context)

def customers(request):
    # Выводит список пользователей
    customers = Customer.objects.all().order_by('date_created')
    context = {'customers': customers}
    return render(request, 'wms/customers.html', context)

def customer(request, customer_id):
    # Выводит одного пользователя и все связанные с ним заявки
    customer = Customer.objects.get(id=customer_id)
    orders = customer.order_set.order_by('-date_in')
    context = {'customer': customer, 'orders': orders}
    return render(request, 'wms/customer.html', context)

def new_customer(request):
    # Создание нового пользователя
    if request.method != 'POST':
        # Данные не отправлялись; создается пустая форма.
        form = CustomerForm()
    else:
        # Отправлены данные POST; обработать данные.
        form = CustomerForm(data=request.POST)
        if form.is_valid():
            new_customer = form.save(commit=False)
            new_customer.save()
            return redirect('wms:customers')

    # Вывести пустую или недействительную форму.
    context = {'form': form}
    return render(request, 'wms/new_customer.html', context)

def storages(request):
    # Выводит список складов
    storages = Storage.objects.all().order_by('address')
    context = {'storages': storages}
    return render(request, 'wms/storages.html', context)

def storage(request, storage_id):
    # Выводит один склад и связанные с ним грузы
    storage = Storage.objects.get(id=storage_id)
    atms = storage.atm_set.order_by('-date_in')
    context = {'storage': storage, 'atms': atms}
    return render(request, 'wms/storage.html', context)

def new_storage(request):
    # Создание нового склада
    if request.method != 'POST':
        # Данные не отправлялись; создается пустая форма.
        form = StorageForm()
    else:
        # Отправлены данные POST; обработать данные.
        form = StorageForm(data=request.POST)
        if form.is_valid():
            new_storage = form.save(commit=False)
            new_storage.save()
            return redirect('wms:storages')

    # Вывести пустую или недействительную форму.
    context = {'form': form}
    return render(request, 'wms/new_storage.html', context)

def atms(request):
    # Выводит список грузов
    atms = Atm.objects.all().order_by('date_in')
    context = {'atms': atms}
    return render(request, 'wms/atms.html', context)

def atm(request, atm_id):
    # Выводит один груз и все связанные с ним заявки
    atm = Atm.objects.get(id=atm_id)
    orders = atm.order_set.order_by('-date_in')
    context = {'atm': atm, 'orders': orders}
    return render(request, 'wms/atm.html', context)

def new_atm(request):
    # Создание нового груза
    if request.method != 'POST':
        # Данные не отправлялись; создается пустая форма.
        form = AtmForm()
    else:
        # Отправлены данные POST; обработать данные.
        form = AtmForm(data=request.POST)
        if form.is_valid():
            new_atm = form.save(commit=False)
            new_atm.save()
            return redirect('wms:atms')

    # Вывести пустую или недействительную форму.
    context = {'form': form}
    return render(request, 'wms/new_atm.html', context)

def orders(request):
    # Выводит список заявок
    orders = Order.objects.all().order_by('date_in')
    context = {'orders': orders}
    return render(request, 'wms/orders.html', context)

def new_order(request):
    # Создание новой заявки
    if request.method != 'POST':
        # Данные не отправлялись; создается пустая форма.
        form = OrderForm()
    else:
        # Отправлены данные POST; обработать данные.
        form = OrderForm(data=request.POST)
        if form.is_valid():
            new_order = form.save(commit=False)
            new_order.save()
            return redirect('wms:orders')

    # Вывести пустую или недействительную форму.
    context = {'form': form}
    return render(request, 'wms/new_order.html', context)

def operations(request):
    # Выводит список операций
    operations = Operation.objects.all().order_by('date_created')
    context = {'operations': operations}
    return render(request, 'wms/operations.html', context)

def new_operation(request):
    # Создание новой операции
    if request.method != 'POST':
        # Данные не отправлялись; создается пустая форма.
        form = OperationForm()
    else:
        # Отправлены данные POST; обработать данные.
        form = OperationForm(data=request.POST)
        if form.is_valid():
            new_operation = form.save(commit=False)
            new_operation.save()
            return redirect('wms:operations')

    # Вывести пустую или недействительную форму.
    context = {'form': form}
    return render(request, 'wms/new_operation.html', context)