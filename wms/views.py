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
        form = ClientForm(request.POST)
        if form.is_valid():
            new_client = form.save(commit=False)
            new_client.save()
            return redirect('wms:clients')

    # Вывести пустую или недействительную форму.
    context = {'form': form}
    return render(request, 'wms/new_client.html', context)

def update_client(request, client_id):
    # Обновление данных по клиенту
    client = Client.objects.get(id=client_id)
    form = ClientForm(instance=client)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('wms:clients')

    context = {'form': form}
    return render(request, 'wms/update_client.html', context)

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
        form = ContractorForm(request.POST)
        if form.is_valid():
            new_contractor = form.save(commit=False)
            new_contractor.save()
            return redirect('wms:contractors')

    # Вывести пустую или недействительную форму.
    context = {'form': form}
    return render(request, 'wms/new_contractor.html', context)

def update_contractor(request, contractor_id):
    # Обновление данных по контрагенту
    contractor = Contractor.objects.get(id=contractor_id)
    form = ContractorForm(instance=contractor)
    if request.method == 'POST':
        form = ContractorForm(request.POST, instance=contractor)
        if form.is_valid():
            form.save()
            return redirect('wms:contractors')
    context = {'form': form}
    return render(request, 'wms/update_contractor.html', context)

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
        form = CustomerForm(request.POST)
        if form.is_valid():
            new_customer = form.save(commit=False)
            new_customer.save()
            return redirect('wms:customers')

    # Вывести пустую или недействительную форму.
    context = {'form': form}
    return render(request, 'wms/new_customer.html', context)

def update_customer(request, customer_id):
    # Обновление данных по пользователю
    customer = Customer.objects.get(id=customer_id)
    form = CustomerForm(instance=customer)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('wms:customers')
    context = {'form': form}
    return render(request, 'wms/update_customer.html', context)

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
        form = StorageForm(request.POST)
        if form.is_valid():
            new_storage = form.save(commit=False)
            new_storage.save()
            return redirect('wms:storages')

    # Вывести пустую или недействительную форму.
    context = {'form': form}
    return render(request, 'wms/new_storage.html', context)

def update_storage(request, storage_id):
    # Обновление данных по складу
    storage = Storage.objects.get(id=storage_id)
    form = StorageForm(instance=storage)
    if request.method == 'POST':
        form = StorageForm(request.POST, instance=storage)
        if form.is_valid():
            form.save()
            return redirect('wms:storages')
    context = {'form': form}
    return render(request, 'wms/update_storage.html', context)

def atms(request):
    # Выводит список грузов
    atms = Atm.objects.all().order_by('date_in')
    context = {'atms': atms}
    return render(request, 'wms/atms.html', context)

def atm(request, atm_id):
    # Выводит один груз и все связанные с ним заявки
    atm = Atm.objects.get(id=atm_id)
    orders = atm.orders.order_by('-date_in')
    context = {'atm': atm, 'orders': orders}
    return render(request, 'wms/atm.html', context)

def new_atm(request):
    # Создание нового груза
    if request.method != 'POST':
        # Данные не отправлялись; создается пустая форма.
        form = AtmForm()
    else:
        # Отправлены данные POST; обработать данные.
        form = AtmForm(request.POST)
        if form.is_valid():
            new_atm = form.save(commit=False)
            new_atm.save()
            return redirect('wms:atms')

    # Вывести пустую или недействительную форму.
    context = {'form': form}
    return render(request, 'wms/new_atm.html', context)

def update_atm(request, atm_id):
    # Обновление данных по грузу
    atm = Atm.objects.get(id=atm_id)
    form = AtmForm(instance=atm)
    if request.method == 'POST':
        form = AtmForm(request.POST, instance=atm)
        if form.is_valid():
            form.save()
            return redirect('wms:atms')
    context = {'form': form}
    return render(request, 'wms/update_atm.html', context)

def delete_atm(request, atm_id):
    # Удаление груза
    atm = Atm.objects.get(id=atm_id)
    if request.method == 'POST':
        atm.delete()
        return redirect('wms:atms')
    context = {'item': atm}
    return render(request, 'wms/delete_atm.html', context)

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
        form = OrderForm(request.POST, request.FILES)
        if form.is_valid():
            new_order = form.save(commit=False)
            new_order.save()
            return redirect('wms:orders')

    # Вывести пустую или недействительную форму.
    context = {'form': form}
    return render(request, 'wms/new_order.html', context)

def update_order(request, order_id):
    # Обновление данных по контрагенту
    order = Order.objects.get(id=order_id)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST, request.FILES, instance=order)
        if form.is_valid():
            form.save()
            return redirect('wms:orders')
    context = {'form': form}
    return render(request, 'wms/update_order.html', context)

def delete_order(request, order_id):
    # Удаление груза
    order = Order.objects.get(id=order_id)
    if request.method == 'POST':
        order.delete()
        return redirect('wms:orders')
    context = {'item': order}
    return render(request, 'wms/delete_order.html', context)