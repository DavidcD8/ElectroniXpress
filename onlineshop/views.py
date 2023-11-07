from .forms import ItemForm
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .models import Item
from .forms import ItemForm
from django.contrib import messages
from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm
from .models import UserProfile
from django.core.paginator import Paginator

# Create your views here.


def ListingView(request):
    return render(request, 'product_list.html')

# View for home page


def Home(request):
    context = {
        'welcome_message': 'Welcome to My Django Web App!',
    }
    return render(request, 'home.html', context)


def Profile(request):
    context = {
        'welcome_message': 'Welcome to My Django Web App!',
    }

    # Retrieve items associated with the logged-in user that are available for sale
    seller_items = Item.objects.filter(seller=request.user, is_available=True)
    seller_items = Item.objects.filter(seller=request.user, is_sold=False)

    # Retrieve items associated with the logged-in user that are marked as sold
    sold_items = Item.objects.filter(seller=request.user, is_sold=True)

    context['seller_items'] = seller_items  # Add seller_items to the context
    context['sold_items'] = sold_items  # Add sold_items to the context

    # Check if a UserProfile instance exists for the current user
    profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Profile updated successfully', extra_tags='profile_updates')

    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    context['form'] = form  # Add the profile form to the context
    context['orders'] = orders

    return render(request, 'profile.html', context)


# view for item list page
def item_list_view(request):
    # Filter out sold items and retrieve only available items
    item_list = Item.objects.filter(is_sold=False).order_by('-created_on')

    # Set the number of items per page
    items_per_page = 20
    paginator = Paginator(item_list, items_per_page)

    # Get the current page number from the request's GET parameters
    page_number = request.GET.get('page')

    # Get the Page object for the current page
    page = paginator.get_page(page_number)

    return render(request, 'item_list.html', {'page': page})


# view for adding item
@login_required
def add_item_view(request):
    if request.method == 'POST':
        item_form = ItemForm(request.POST, request.FILES)

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


def update_bag(request, item_id):
    if request.method == 'POST':
        form = UpdateQuantityForm(request.POST)
        if form.is_valid():
            new_quantity = form.cleaned_data['quantity']

            # Update the bag item's quantity
            bag = request.session.get('bag', {})
            bag[item_id] = new_quantity
            request.session['bag'] = bag
            request.session.modified = True

            # Recalculate bag contents (subtotal and total)
            total = Decimal(0)
            for item_id, quantity in bag.items():
                item = get_object_or_404(Item, pk=item_id)
                total += item.price * quantity

            subtotal = total  # Calculate the subtotal as the total amount in Euros

            grand_total = subtotal  # You can include additional costs like delivery here if needed

            # Redirect to the cart or bag view after updating
            return redirect('view_bag')

    # Handle other cases or errors as needed
    return redirect('view_bag')


# view for item detail


def item_detail(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    return render(request, 'item_detail.html', {'item': item})

# view for item list


def item_list(request):
    items = Item.objects.all()
    return render(request, 'item_list.html', {'items': items})
