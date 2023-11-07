from django.contrib import admin
from .models import UserProfile
from django.contrib.auth.models import User


class ProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False


admin.site.unregister(User)
admin.site.register(UserProfile)
