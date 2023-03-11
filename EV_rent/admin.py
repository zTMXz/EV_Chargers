from django.contrib import admin
from .models import Car, ServiceRequest

admin.site.register(Car)
admin.site.register(ServiceRequest)