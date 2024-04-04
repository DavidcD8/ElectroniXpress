from django.shortcuts import render

from .models import FAQ


def faq(request):
    """View for faq page"""
    faqs = FAQ.objects.all()
    template = "faq.html"
    context = {
        "faqs": faqs,
    }
    return render(request, template, context)
