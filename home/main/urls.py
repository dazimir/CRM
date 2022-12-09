from django.urls import path
from . import views
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', views.index, name='index'),
    path('admin', views.admin, name='admin'),
    path('Priem_zayavok', views.input_task, name='input_task'),
    path('Otchet_po_zayavkam', views.report_task, name='report_task'),
    path('Status_zayavok', views.status_task, name='status_task'),
    path('Customer_card', views.customer_card, name='customer_card'),
    path('Input_new_task', views.input_new_task, name='input_new_task'),
    path('<int:pk>/card-delete', views.CardsDeleteView.as_view(), name='card-delete'),
    path('<int:pk>/card-update', views.CardsUpdateView.as_view(), name='card-update'),

    path('Input_FL', views.input_FL, name='input_FL'),
    path('Input_UL', views.input_UL, name='input_UL'),
    path('Settings_CRM', views.settings_crm, name='settings_crm'),
]
