from django.db import models

#Электромобили (ид, Модель, Тип зарядки, кол-во л.с., сидячих мест, цена аренды)

class Car(models.Model):
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
    url_page = models.CharField(max_length=50)
    is_broken = models.BooleanField(default=False)
    is_rented = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.car_brand} {self.model}"


class ServiceRequest(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    car_model = models.CharField(max_length=100)
    description = models.TextField()
    photos = models.ImageField(upload_to='repair_images/%Y/%m/%d/', blank=True)
    is_broken = models.BooleanField(default=False)
    is_rented = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class RentalRequest(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    car_model = models.CharField(max_length=100)
    num_days = models.IntegerField()
    is_broken = models.BooleanField(default=False)
    is_rented = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.car_model}"
