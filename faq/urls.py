from django.urls import path
from . import views
from .views import faq

urlpatterns = [
    path("", faq, name="faq"),
]