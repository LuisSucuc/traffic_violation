from django.contrib import admin
from .models import Person, Vehicle, Officer, Brand, Color


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name', 'email')
    list_filter = ('name',)


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('plate', 'brand', 'color', 'person')
    search_fields = ('plate', 'brand', 'color', 'person')
    list_filter = ('brand', 'color', 'person')

    fieldsets = (
        ('General Information', {
            'fields': ('plate', 'brand', 'color')
        }),
        ('Owner Information', {
            'fields': ('person',)
        }),
    )


@admin.register(Officer)
class OfficerAdmin(admin.ModelAdmin):
    list_display = ('name', 'id_number')
    search_fields = ('name', 'id_number')
    list_filter = ('name',)

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)

@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)



