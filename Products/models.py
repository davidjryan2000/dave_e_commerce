from  __future__ import unicode_literals

from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='images')
    tag = models.CharField(max_length=20, default='')

    def __str__(self):
        return self.name