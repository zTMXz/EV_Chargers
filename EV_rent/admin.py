from django.contrib import admin
from .models import Car, ServiceRequest, RentalRequest, RentalHistory, ServiceHistory

admin.site.register(Car)
admin.site.register(ServiceRequest)
admin.site.register(RentalRequest)
admin.site.register(RentalHistory)
admin.site.register(ServiceHistory)