from .forms import ItemForm, LocationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .models import Item
from .forms import ItemForm
from .models import Location
from django.contrib import messages
from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.


def ListingView(request):
    return render(request, 'product_list.html')

# View for home page


def Home(request):
    context = {
        'welcome_message': 'Welcome to My Django Web App!',
    }
    return render(request, 'home.html', context)

# view for adding item


@login_required
def add_item_view(request):
    if request.method == 'POST':
        item_form = ItemForm(request.POST, request.FILES)
        location_form = LocationForm(request.POST)

        if item_form.is_valid() and location_form.is_valid():
            item = item_form.save(commit=False)
            item.seller = request.user

            # Get the selected location ID
            selected_location_id = location_form.cleaned_data.get('location')

            try:
                # This will Makes sure that the user selected_location_id is a valid integer
                selected_location_id = int(selected_location_id)
                selected_location = Location.objects.get(
                    pk=selected_location_id)
                item.location = selected_location
                item.save()
                messages.success(request, 'Item added successfully!')
                return redirect('item_list')
            except (ValueError, Location.DoesNotExist):
                # Handle in case that the selected location does not exist or the ID is invalid
                messages.error(
                    request, 'Error in form submission. Please check your inputs.')
        else:
            messages.error(
                request, 'Error in form submission. Please check your inputs.')
    else:
        item_form = ItemForm()
        location_form = LocationForm()

    return render(request, 'add_item.html', {'item_form': item_form, 'location_form': location_form})


def search_results(request):
    query = request.GET.get('query')
    results = Item.objects.filter(name__icontains=query)
    return render(request, 'search_results.html', {'results': results, 'query': query})


def view_bag(request):
    # Retrieve the cart data from the session
    bag = request.session.get('bag', {})

    # Create a list to store item dictionaries with quantity and total price
    bag_items = []

    # Calculate the total price for each item and add it to the item dictionary
    for item_id, quantity in bag.items():
        item = get_object_or_404(Item, pk=item_id)
        total_price = item.price * quantity
        item_dict = {
            'item': item,
            'quantity': quantity,
            'total_price': total_price,
        }
        bag_items.append(item_dict)

    context = {
        'bag_items': bag_items,
    }

    return render(request, 'bag/bag.html', context)

# view for item detail


def item_detail(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    return render(request, 'item_detail.html', {'item': item})

# view for item list


def item_list(request):
    items = Item.objects.all()
    return render(request, 'item_list.html', {'items': items})


