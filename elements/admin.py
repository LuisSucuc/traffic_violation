from django.contrib import admin
from .models import Person, Vehicle, Officer, Brand, Color
from django.contrib.auth.admin import UserAdmin


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


@admin.register(Officer)
class OfficerAdmin(UserAdmin):
    # Fields to be displayed in the edit page
    fieldsets = (
        (("Personal info"), {"fields": ("name", "username", "email")}),
        (
            ("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups"
                ),
            },
        ),
        ("Password", {"fields": ("password",)}),
    )

    # Fields to be displayed in the add page
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("name", "email", "username", "password1", "password2", "groups"),
            },
        ),
    )

    def officer_id(self, obj):
        '''
        Add a custom field to the list display
        '''
        return obj.id

    # Add better description to the id field
    officer_id.short_description = 'Officer ID'

    # Fields to be displayed in the list page
    list_display = ("officer_id", "name", "email",
                    "username", "is_staff", "is_superuser")
