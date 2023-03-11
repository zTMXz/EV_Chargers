from django.urls import path
from . import views

urlpatterns = [
    path('', views.car_list, name='rent'),
    path('service_request/', views.service_request, name='service_request'),
    path('rental_request/', views.rental_request, name='rental_request'),
    path('service_request_success/', views.service_request_success, name='service_request_success'),
    path('<str:model>/', views.get_model_info, name='model_info'),
]

