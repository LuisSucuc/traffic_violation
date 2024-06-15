from django.contrib import admin
from .models import Infraction


@admin.register(Infraction)
class InfractionAdmin(admin.ModelAdmin):
    list_display = ('vehicle', 'timestamp', 'comments', 'officer')
    search_fields = ('vehicle', 'timestamp', 'comments', 'officer')
    list_filter = ('vehicle', 'timestamp', 'comments', 'officer')
