from django.contrib import admin
from .models import UserProfile
from django.contrib.auth.models import User
from django.contrib import admin
from .models import Item


class ProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False


class ItemAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "price",
        "seller",
        "is_sold",
    )

    list_filter = ("is_sold", "seller")
    search_fields = ("name", "seller__username")
    ordering = ("name",)


admin.site.register(Item, ItemAdmin)
admin.site.unregister(User)
admin.site.register(UserProfile)
