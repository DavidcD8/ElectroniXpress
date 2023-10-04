from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class City(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=254)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    image = models.ImageField()
    seller = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="items")
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    create_on = models.DateTimeField(auto_now=True)
    is_sold = models.BooleanField(default=False)

    def __str__(self):
        return self.name


