from django.db import models

class Registration(models.Model):
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.login


class User(models.Model):
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=50)