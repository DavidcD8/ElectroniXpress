from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=254)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    image = models.ImageField()
    seller = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="items")
    create_on = models.DateTimeField(auto_now=True)
    is_sold = models.BooleanField(default=False)
