from django.urls import path
from .views import LoadInfractionView

urlpatterns = [
    path('cargar_infraccion/', LoadInfractionView.as_view(),
         name='cargar_infraccion'),
]