from django.contrib import admin
from .models import UserProfile
from django.contrib.auth.models import User
from django.contrib import admin
from .models import Item


class ProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False


admin.site.unregister(User)
admin.site.register(UserProfile)


class ItemAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'price',
        'seller',
        'location',
        'is_available',
        'is_sold',
    )

    list_filter = ('is_available', 'is_sold', 'seller', 'location')
    search_fields = ('name', 'seller__username', 'location__name')
    ordering = ('name',)


admin.site.register(Item, ItemAdmin)
