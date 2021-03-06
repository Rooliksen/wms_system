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

class Size(models.TextChoices):
    # Габарит, размер
    EUR = 'EUR', 'Габарит EUR'
    FIN = 'FIN', 'НЕГабарит FIN'

class Status(models.TextChoices):
    # Статус груза
    in_store = 'Принят', 'Принят'
    out = 'Отгружен', 'Отгружен'
    in_reserve = 'Резерв', 'Резерв'

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

class OrderStatus(models.TextChoices):
    # Статус заявки от клиента
    in_process = 'Активна', 'Активна'
    done = 'Закрыта', 'Закрыта'
    canceled = 'Отменена', 'Отменена'
    draft = 'Черновик', 'Черновик'

class Atm(models.Model):
    # Груз, банкомат
    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.in_reserve,
    )
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
    storage = models.ForeignKey(Storage, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    serial_num = models.CharField(max_length=200)
    atm_id = models.CharField(max_length=200, blank=True, null=True)
    size = models.CharField(
        max_length=10,
        choices=Size.choices,
        default=Size.EUR,
    )
    commentary = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.serial_num

class Order(models.Model):
    # Заявка от Клиента
    logistic_order = models.CharField(max_length=200)
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, blank=True, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    storage = models.ForeignKey(Storage, on_delete=models.SET_NULL, null=True)
    status = models.CharField(
        max_length=10,
        choices=OrderStatus.choices,
        default=OrderStatus.draft,
    )
    date_in = models.DateField('Дата приема', blank=True, null=True)
    date_out = models.DateField('Дата отгрузки', blank=True, null=True)
    driver = models.CharField(max_length=200, blank=True, null=True)
    driver_car = models.CharField(max_length=200, blank=True, null=True)
    storage_order = models.CharField(max_length=200, blank=True, null=True)
    date_created = models.DateTimeField('date published', auto_now_add=True)
    
    def __str__(self):
        return self.logistic_order

class OrderItem(models.Model):
    # Элемент заявки
    atm = models.ForeignKey(Atm, on_delete=models.CASCADE, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

class AtmPhoto(models.Model):
    # Фотография в заявке
    description = models.CharField(max_length=200, blank=True, null=True)
    atm = models.ForeignKey(Atm, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(blank=True, null=True)

