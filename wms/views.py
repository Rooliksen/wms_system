from django.shortcuts import render
from .models import *

def index(request):
    # Домашняя страница приложения WMS
    return render(request, 'wms/index.html')

def clients(request):
    # Выводит список клиентов
    clients = Client.objects.all().order_by('pub_date')
    context = {'clients': clients}
    return render(request, 'wms/clients.html', context)

def contractors(request):
    # Выводит список контрагентов
    contractors = Contractor.objects.all().order_by('pub_date')
    context = {'contractors': contractors}
    return render(request, 'wms/contractors.html', context)

def customers(request):
    # Выводит список контрагентов
    customers = Customer.objects.all().order_by('date_created')
    context = {'customers': customers}
    return render(request, 'wms/customers.html', context)

def storages(request):
    # Выводит список контрагентов
    storages = Storage.objects.all().order_by('address')
    context = {'storages': storages}
    return render(request, 'wms/storages.html', context)
