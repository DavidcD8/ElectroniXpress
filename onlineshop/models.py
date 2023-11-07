from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils import timezone
from django_countries.fields import CountryField

# Create your models here.
CONDITION_CHOICES = (
    ("new", "New"),
    ("used", "Used"),
)


class Item(models.Model):
    name = models.CharField(max_length=254)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    sku = models.CharField(max_length=254, null=True, blank=True)
    image = models.ImageField()
    seller = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="items")
    is_available = models.BooleanField(default=True)
    is_sold = models.BooleanField(default=False)
    quantity = models.PositiveIntegerField(default=1)
    condition = models.CharField(
        max_length=50, choices=CONDITION_CHOICES, default='new')

    def mark_as_sold(self):
        self.is_available = False
        self.is_sold = True
        self.save()

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    """
    A user profile model for maintaining default delivery information and order history
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(
        upload_to='profile_pictures/', blank=True, null=True)
    default_phone_number = models.CharField(
        max_length=20, null=True, blank=True)
    default_street_address1 = models.CharField(
        max_length=80, null=True, blank=True)
    default_street_address2 = models.CharField(
        max_length=80, null=True, blank=True)
    default_town_or_city = models.CharField(
        max_length=40, null=True, blank=True)
    default_county = models.CharField(max_length=80, null=True, blank=True)
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_country = CountryField(
        blank_label='Country', null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()
