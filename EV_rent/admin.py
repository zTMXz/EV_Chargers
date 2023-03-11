from django.contrib import admin
from .models import Car, ServiceRequest, RentalRequest

admin.site.register(Car)
admin.site.register(ServiceRequest)
admin.site.register(RentalRequest)