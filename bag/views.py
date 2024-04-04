from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from onlineshop.models import Item


def view_bag(request):
    """A view that renders the bag contents page"""

    return render(request, "bag/bag.html")


def add_to_bag(request, item_id):
    """Add a quantity of the specified product to the shopping bag"""
    item = get_object_or_404(Item, pk=item_id)
    quantity = int(request.POST.get("quantity"))

    bag = request.session.get("bag", {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session["bag"] = bag
    messages.success(request, f"{item.name} Added to bag.")
    return redirect(view_bag)


@login_required
def remove_from_bag(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    bag = request.session.get("bag", {})

    if str(item_id) in bag:
        bag.pop(str(item_id))

        # Update the session
        request.session["bag"] = bag
    messages.success(request, f"{item.name} Deleted From bag.")

    return redirect("view_bag")
