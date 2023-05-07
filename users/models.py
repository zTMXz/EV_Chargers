from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    email = models.EmailField(
        _("email address"),
        unique=True
    )

    driver_license = models.ImageField(upload_to='users/driver_license', blank=True)
    driver_license_with_owner = models.ImageField(upload_to='users/driver_license', blank=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", "driver_license", "driver_license", "driver_license_with_owner"]
