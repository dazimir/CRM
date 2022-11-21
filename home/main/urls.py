from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('Priem_zayavok', views.input_task, name='input_task'),
    path('Otchet_po_zayavkam', views.report_task, name='report_task'),
    path('Status_zayavok', views.status_task, name='status_task'),
]
