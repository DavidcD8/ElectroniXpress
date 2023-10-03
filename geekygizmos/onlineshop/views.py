from django.shortcuts import render
from django.views import generic
from .models import Product
from django.views.generic import DetailView

# Create your views here.


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'

    def get(self, request, *args, **kwargs):

        return super().get(request, *args, **kwargs)


def ListingView(request):
    return render(request, 'product_list.html')
