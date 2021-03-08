from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Client(models.Model):
    # Клиент
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', auto_now_add=True)

    def __str__(self):
        return self.name

class Contractor(models.Model):
    # Контрагент
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', auto_now_add=True)

    def __str__(self):
        return self.name

class Size(models.Model):
    # Габарит, размер
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', auto_now_add=True)

    def __str__(self):
        return self.name

class Status(models.Model):
    # Статус
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', auto_now_add=True)

    def __str__(self):
        return self.name

class Customer(models.Model):
    # Пользователь
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, blank=True)
    post = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=200, blank=True)
    email = models.CharField(max_length=200, blank=True)
    profile_pic = models.CharField(max_length=200, blank=True)
    date_created = models.DateTimeField('date published', auto_now_add=True)

    def __str__(self):
        return self.name

class OperationContractor(models.Model):
    # Операции с контрагентом, услуги по договору ОПЕРАТОР-КОНТРАГЕНТ
    contractor = models.ForeignKey(Contractor, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    cost = models.DecimalField(max_digits=9999, decimal_places=2, null=True)
    date_created = models.DateTimeField('date published', auto_now_add=True)

    def __str__(self):
        return self.name

class OperationClient(models.Model):
    # Операции с клиентом, услуги по договору КЛИЕНТ-ОПЕРАТОР
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    cost = models.DecimalField(max_digits=9999, decimal_places=2, null=True)
    date_created = models.DateTimeField('date published', auto_now_add=True)

    def __str__(self):
        return self.name

class Storage(models.Model):
    # Склад, текущее местонахождение
    contractor = models.ForeignKey(Contractor, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200)
    rate_pallet = models.DecimalField(max_digits=9999, decimal_places=2, null=True)
    rate_oversize_pallet = models.DecimalField(max_digits=9999, decimal_places=2, null=True)
    rate_volume = models.DecimalField(max_digits=9999, decimal_places=2, null=True)
    rate_in = models.DecimalField(max_digits=9999, decimal_places=2, null=True)
    rate_out = models.DecimalField(max_digits=9999, decimal_places=2, null=True)
    rate_oversize_in = models.DecimalField(max_digits=9999, decimal_places=2, null=True)
    rate_oversize_out = models.DecimalField(max_digits=9999, decimal_places=2, null=True)

    def __str__(self):
        return self.address

class Atm(models.Model):
    # Груз, банкомат
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True)
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
    storage = models.ForeignKey(Storage, on_delete=models.SET_NULL, null=True)
    date_in = models.DateTimeField('Дата приема')
    date_out = models.DateTimeField('Дата отгрузки')
    name = models.CharField(max_length=200)
    serial_num = models.CharField(max_length=200)
    atm_id = models.CharField(max_length=200)
    size = models.ForeignKey(Size, on_delete=models.SET_NULL, null=True)
    commentary = models.CharField(max_length=200)

    def __str__(self):
        return self.serial_num

class OrderClient(models.Model):
    # Заявка от Клиента
    logistic_order = models.CharField(max_length=200)
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
    atm = models.ForeignKey(Atm, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=200)
    date_in = models.DateTimeField('Дата приема')
    date_out = models.DateTimeField('Дата отгрузки')
    storage = models.ForeignKey(Storage, on_delete=models.SET_NULL, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    operation_client = models.ForeignKey(OperationClient, on_delete=models.SET_NULL, null=True)
    date_created = models.DateTimeField('date published', auto_now_add=True)
    
    def __str__(self):
        return self.logistic_order

class OrderContractor(models.Model):
    # Заявка для Контрагента
    storage_order = models.CharField(max_length=200)
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
    date_in = models.DateTimeField('Дата приема')
    date_out = models.DateTimeField('Дата отгрузки')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    storage = models.ForeignKey(Storage, on_delete=models.SET_NULL, null=True)
    atm = models.ForeignKey(Atm, on_delete=models.SET_NULL, null=True)
    operation_contractor =  models.ForeignKey(OperationContractor, on_delete=models.SET_NULL, null=True)
    driver = models.CharField(max_length=200)
    driver_car = models.CharField(max_length=200)
    date_created = models.DateTimeField('date published', auto_now_add=True)
    
    def __str__(self):
        return self.storage_order