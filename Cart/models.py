from __future__ import unicode_literals

from django.db import models
from Products.models import Product
from django.contrib.auth.models import User

# Create your models here.
class CartItem(models.Model):
    user = models.ForeignKey(User)
    product = models.ForeignKey(Product)
    quantity = models.IntegerField()
    order = models.CharField(max_length=40, default='')

    def __str__(self):
        return "{0} ({1})".format(self.product.name, self.quantity)

