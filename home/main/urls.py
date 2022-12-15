from django.urls import path
from . import views
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', views.admin, name='admin'),
    path('Priem_zayavok', views.input_new_task, name='input_new_task'),
    path('Otchet_po_zayavkam', views.report_task, name='report_task'),
    path('Status_zayavok', views.status_task, name='status_task'),

    path('Customer_card_FL', views.customer_card_FL, name='customer_card_FL'),
    path('<int:pk>/card-delete_FL', views.CardsDeleteView_FL.as_view(), name='card-delete_FL'),
    path('<int:pk>/card-update_FL', views.CardsUpdateView_FL.as_view(), name='card-update_FL'),

    path('Customer_card_UL', views.customer_card_UL, name='customer_card_UL'),
    path('<int:pk>/card-delete_UL', views.CardsDeleteView_UL.as_view(), name='card-delete_UL'),
    path('<int:pk>/card-update_UL', views.CardsUpdateView_UL.as_view(), name='card-update_UL'),

    path('Input_new_task', views.input_new_task, name='input_new_task'),

    path('Input_FL', views.input_FL, name='input_FL'),
    path('Input_UL', views.input_UL, name='input_UL'),

    path('Settings_CRM', views.settings_crm, name='settings_crm'),
    path('login', views.login_crm, name='login_crm'),

]
