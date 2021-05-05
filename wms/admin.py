from django.contrib import admin
from .models import *

class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'pub_date')

class ContractorAdmin(admin.ModelAdmin):
    list_display = ('name', 'pub_date')

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'post', 'phone', 'email', 'date_created')

class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'logistic_order', 'client', 'customer',
        'storage', 'status', 'date_in',
        'date_out', 'driver',
        'driver_car', 'storage_order', 'date_created'
        )

class AtmAdmin(admin.ModelAdmin):
    list_display = ('status', 'client', 'storage', 'name', 'serial_num', 'atm_id', 'size', 'commentary')

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('atm', 'order', 'date_added')

admin.site.register(Client, ClientAdmin)
admin.site.register(Contractor, ContractorAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Storage)
admin.site.register(Atm, AtmAdmin)
admin.site.register(Order, OrderAdmin)
