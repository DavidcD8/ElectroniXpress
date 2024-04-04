from django.urls import path

from . import views
from .webhooks import webhook

urlpatterns = [
    path("checkout/", views.checkout, name="checkout"),
    path("success/<order_number>", views.checkout_success, name="success"),
    path("wh/", webhook, name="webhook"),
]
