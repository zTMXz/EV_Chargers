from django.db import models
from django.urls import reverse
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from datetime import datetime

from users.models import User


# Электромобили (ид, Модель, Тип зарядки, кол-во л.с., сидячих мест, цена аренды)

class Car(models.Model):
    car_full_name = models.CharField(max_length=100)
    car_brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    charge_type = models.CharField(max_length=100)
    horse_power = models.IntegerField()
    num_sits = models.IntegerField()
    range_km = models.IntegerField()
    rent_price = models.FloatField()
    year = models.IntegerField()
    image = models.ImageField(upload_to='image_cars', blank=True, null=True)
    description = models.TextField()
    url_page = models.SlugField(max_length=50, unique=True)
    is_broken = models.BooleanField(default=False)
    is_rented = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("model_info", kwargs={"slug": self.url_page})

    def __str__(self):
        return f"{self.car_brand} {self.model}"


class ServiceRequest(models.Model):
    person = models.ForeignKey(User, on_delete=models.CASCADE)
    car_model = models.ForeignKey(Car, on_delete=models.CASCADE)
    description = models.TextField()
    photos = models.ImageField(upload_to='repair_images/%Y/%m/%d/', blank=True)

    def __str__(self):
        return f"{self.person.first_name} {self.person.last_name} сообщил о поломке {self.car_model}"


class RentalRequest(models.Model):
    person = models.ForeignKey(User, on_delete=models.CASCADE)
    car_model = models.ForeignKey(Car, on_delete=models.CASCADE)
    num_days = models.IntegerField()

    def __str__(self):
        return f"{self.person.first_name} {self.person.last_name} арендовал {self.car_model}"

class RentalHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_date = models.DateTimeField(default=datetime.now, blank=True)
    end_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}, аренда {self.car} от {self.start_date.strftime('%Y-%m-%d')}"
class ServiceHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.now, blank=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}, поломка {self.car} от {self.date.strftime('%Y-%m-%d')}"



@receiver(pre_delete, sender=RentalRequest)
def set_car_rent_as_available(sender, instance, **kwargs):
    car = instance.car_model
    car.is_rented = False
    car.save()


@receiver(pre_delete, sender=ServiceRequest)
def set_car_broken_as_available(sender, instance, **kwargs):
    car = instance.car_model
    car.is_broken = False
    car.save()


