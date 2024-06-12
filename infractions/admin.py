from django.contrib import admin
from .models import Infraction


@admin.register(Infraction)
class InfractionAdmin(admin.ModelAdmin):
    list_display = ('vehicle', 'timestamp', 'comments')
    search_fields = ('vehicle', 'timestamp', 'comments')
    list_filter = ('vehicle', 'timestamp', 'comments')
