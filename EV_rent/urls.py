from django.urls import path
from . import views

urlpatterns = [
    path('', views.CarList.as_view(), name='rent'),
    path('service_request/', views.service_request, name='service_request'),
    path('rental_request/<int:car_id>', views.rental_request, name='rental_request'),
    path('service_request_success/', views.service_request_success, name='service_request_success'),
    path('<slug:slug>/', views.ModelDetailView.as_view(), name='model_info'),
]

