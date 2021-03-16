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
    list_display = ('status', 'client', 'storage', 'date_in', 'date_out', 'name', 'serial_num', 'atm_id', 'size', 'commentary')

admin.site.register(Client, ClientAdmin)
admin.site.register(Contractor, ContractorAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Storage)
admin.site.register(Atm, AtmAdmin)
admin.site.register(Order, OrderAdmin)
