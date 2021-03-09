from django.shortcuts import render, redirect
from .models import *
from .forms import *

def index(request):
    # Домашняя страница приложения WMS
    return render(request, 'wms/index.html')

def clients(request):
    # Выводит список клиентов
    clients = Client.objects.all().order_by('pub_date')
    context = {'clients': clients}
    return render(request, 'wms/clients.html', context)

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

def client_orders(request):
    # Выводит список контрагентов
    client_orders = OrderClient.objects.all().order_by('date_in')
    context = {'client_orders': client_orders}
    return render(request, 'wms/client_orders.html', context)