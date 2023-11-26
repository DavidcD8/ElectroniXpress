
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Item
from .forms import ItemForm
from .models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .forms import EditItemForm
from .forms import MarkItemAsSoldForm
from .forms import CheckoutForm
from .forms import UpdateQuantityForm
from decimal import Decimal
from django.utils import timezone
from .forms import UserProfileForm
from django.contrib import messages


# View For 404 Page
def handler404(request, exception):
    return render(request, '404.html', status=404)




# View for the listings page
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

    # Retrieve items associated with the logged- d user that are available for sale
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


# view for item detail page


def item_detail(request, item_id):
    item = get_object_or_404(Item, id=item_id)

    return render(request, 'item_detail.html', {'item': item})

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

# view for success page


def success_view(request):
    return render(request, 'success.html')

    # To edit the item being sold


@login_required
def edit_item_view(request, item_id):
    item = get_object_or_404(Item, id=item_id, seller=request.user)

    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = EditItemForm(instance=item)

    return render(request, 'edit_item.html', {'form': form, 'item': item})


@login_required
def delete_item_view(request, item_id):
    item = get_object_or_404(Item, id=item_id, seller=request.user)

    if request.method == 'POST':
        # Update the item's status to "sold"  
        item.status = 'deleted'  # Update the status to 'deleted' or another value
        item.delete()
        messages.success(request, 'Item marked as deleted successfully!')

        # Redirect back to the user's profile page or another page
        return redirect('profile')

    return render(request, 'delete_item.html', {'item': item})


@login_required
def mark_as_sold(request, item_id):
    # Get the item from the database
    item = get_object_or_404(Item, id=item_id)
    item = get_object_or_404(Item, id=item_id, seller=request.user)

    if request.method == 'POST':
        item.is_sold = True
        item.save()
        messages.success(request, 'Item marked as sold successfully!')

    # Update the item's status to "sold"  
    item.status = 'sold'
    item.save()

    # Redirect back to the user's profile page or some other page
    return redirect('profile')


def view_other_profile(request, username):
    # Get the user profile of the user with the given username
    user_profile = get_object_or_404(UserProfile, user__username=username)

    # Get the items associated with the user and that are available for sale
    user_items = Item.objects.filter(
        seller=user_profile.user, is_available=True)

    context = {
        'user_profile': user_profile,
        'user_items': user_items,
    }

    return render(request, 'other_profile.html', context)
 

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


@login_required
def add_item_view(request):
    if request.method == 'POST':
        item_form = ItemForm(request.POST, request.FILES)

        if item_form.is_valid():
            # Process the form data and save the item
            item = item_form.save(commit=False)
            item.seller = request.user
            item.save()
            item_form.save_m2m()
            messages.success(request, 'Item added successfully!')
            # Redirect to the item list page after successfully adding an item
            return redirect('item_list')
        else:
            messages.error(
                request, 'Form submission failed. Please check your input.')

    else:
        item_form = ItemForm()

    return render(request, 'add_item.html', {'item_form': item_form})


def search_results(request):
    query = request.GET.get('query')
    results = Item.objects.filter(name__icontains=query)
    return render(request, 'search_results.html', {'results': results, 'query': query})


def process_checkout_view(request):
    if request.method == 'POST':
        form = CheckoutForm(request.POST)

        if form.is_valid():
            # Redirect to a success page after successful checkout
            messages.success(request, 'Order placed successfully!')
            return redirect('order_success')
        else:
            # Form data is invalid, display error messages
            messages.error(
                request, 'Invalid payment details. Please check and try again.')

    else:
        form = CheckoutForm()

    return render(request, 'checkout.html', {'form': form})
