from django.shortcuts import render, redirect
from django.views import generic
from .models import Product
from django.views.generic import DetailView
from .forms import ProductForm

# Create your views here.


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'

    def get(self, request, *args, **kwargs):

        return super().get(request, *args, **kwargs)


def ListingView(request):
    return render(request, 'product_list.html')


def CreateAd(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            Product = form.save(commit=False)
            Product.seller = request.User
            Product.save()
            return redirect('prouct_list')
    else:
        form = ProductForm()

    return render(request, 'create_ad.html', {'form': form})
