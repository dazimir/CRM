from django.urls import path
from . import views
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', views.index, name='index'),
    path('Priem_zayavok', views.input_task, name='input_task'),
    path('Otchet_po_zayavkam', views.report_task, name='report_task'),
    path('Status_zayavok', views.status_task, name='status_task'),
    path('Customer_card', views.customer_card, name='customer_card'),
    path('<int:pk>/card-delete', views.CardsDeleteView.as_view(), name='card-delete'),
    path('<int:pk>/card-update', views.CardsUpdateView.as_view(), name='card-update'),

    path('admin', views.admin, name='admin'),
]
