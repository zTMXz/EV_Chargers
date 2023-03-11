# from django.contrib.auth.models import User, Group, Permission
#
# from django.contrib.auth.models import AbstractUser
# from django.db import models
#
# class User(models.Model):
#     # ... other fields
#     groups = models.ManyToManyField(
#         Group,
#         related_name='auth_user_groups',
#         blank=True,
#         help_text=(
#             'The groups this user belongs to. A user will get all permissions granted to each of their groups.'
#         ),
#     )
#     user_permissions = models.ManyToManyField(
#         Permission,
#         related_name='auth_user_user_permissions',
#         blank=True,
#         help_text=('Specific permissions for this user.'),
#     )


from django.db import models

class User(models.Model):
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=50)