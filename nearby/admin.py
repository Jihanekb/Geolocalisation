from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Shop, Hotel, Bank, Restaurant, Somewhere

# Register your models here.
@admin.register(Shop)
@admin.register(Hotel)
@admin.register(Bank)
@admin.register(Restaurant)
@admin.register(Somewhere)
class ShopAdmin(OSMGeoAdmin):
    list_display = ('name','location')
