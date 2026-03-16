from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=20, blank=True)
    gender_choices = [('M', 'Мужской'), ('F', 'Женский')]
    gender = models.CharField(max_length=1, choices=gender_choices, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    client_type_choices = [('regular', 'Обычный'), ('wholesale', 'Оптовик')]
    client_type = models.CharField(max_length=10, choices=client_type_choices, default='regular')