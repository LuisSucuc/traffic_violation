from django.urls import path
from .views import LoadInfractionView, GenerateReportView

urlpatterns = [
    path('cargar_infraccion/', LoadInfractionView.as_view(),
         name='cargar_infraccion'),
    path('generar_informe/', GenerateReportView.as_view(), name='generar_informe'),

]