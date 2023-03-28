from modeltranslation.translator import register, TranslationOptions
from .models import Car, ServiceRequest, RentalRequest

@register(Car)
class CarTranslationOptions(TranslationOptions):
    fields = ['description']

@register(ServiceRequest)
class ServiceRequestTranslationOptions(TranslationOptions):
    fields = ['description']

