from django.contrib import admin
from .models import Person, Vehicle, Officer


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name', 'email')
    list_filter = ('name',)


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('plate', 'brand', 'color', 'person')
    search_fields = ('plate', 'brand', 'color', 'person__name')
    list_filter = ('brand', 'color')


@admin.register(Officer)
class OfficerAdmin(admin.ModelAdmin):
    list_display = ('name', 'id_number')
    search_fields = ('name', 'id_number')
    list_filter = ('name',)



