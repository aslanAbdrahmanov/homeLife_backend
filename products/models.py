# products/models.py

from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    is_new = models.BooleanField(default=False)
    is_popular = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name