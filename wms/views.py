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
    # Выводит одну тему и все её записи
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
    # Выводит одну тему и все её записи
    contractor = Contractor.objects.get(id=contractor_id)
    storages = Storage.objects.get(id=contractor_id)
    atms = storages.atm_set.order_by('-date_in')
    context = {'contractor': contractor, 'storages': storages, 'atms': atms}
    return render(request, 'wms/contractor.html', context)

def new_contractor(request):
    # Создание нового клиента
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
    # Выводит список контрагентов
    customers = Customer.objects.all().order_by('date_created')
    context = {'customers': customers}
    return render(request, 'wms/customers.html', context)

def customer(request, customer_id):
    # Выводит одну тему и все её записи
    customer = Customer.objects.get(id=customer_id)
    orders = customer.order_set.order_by('-date_in')
    context = {'customer': customer, 'orders': orders}
    return render(request, 'wms/customer.html', context)

def new_customer(request):
    # Создание нового клиента
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
    # Выводит список контрагентов
    storages = Storage.objects.all().order_by('address')
    context = {'storages': storages}
    return render(request, 'wms/storages.html', context)

def new_storage(request):
    # Создание нового клиента
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
    # Выводит список контрагентов
    atms = Atm.objects.all().order_by('date_in')
    context = {'atms': atms}
    return render(request, 'wms/atms.html', context)

def new_atm(request):
    # Создание нового клиента
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
    # Выводит список контрагентов
    orders = Order.objects.all().order_by('date_in')
    context = {'orders': orders}
    return render(request, 'wms/orders.html', context)