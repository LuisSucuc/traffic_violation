from django.urls import path
from .views import home_view, view_infraction_records, view_create_infraction

urlpatterns = [
    path('', home_view, name='home'),
    path('my_infractions/', view_infraction_records,
         name='my_infractions'),
    path('create_infraction/', view_create_infraction,
         name='create_infraction'),
]
