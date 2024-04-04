from decimal import Decimal

from django.conf import settings
from django.shortcuts import get_object_or_404

from onlineshop.models import Item  # Make sure to import your Item model


def bag_contents(request):
    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get("bag", {})

    for item_id, quantity in bag.items():
        item = get_object_or_404(Item, pk=item_id)
        total += item.price * quantity
        product_count += quantity
        bag_items.append(
            {
                "item_id": item_id,
                "quantity": quantity,
                "item": item,
                "total_price": item.price
                * quantity,  # Calculate total price for each item
            }
        )

    subtotal = total  # Calculate the subtotal as the total amount in Euros

    # Calculate delivery cost
    if subtotal < settings.FREE_DELIVERY_THRESHOLD:
        delivery = subtotal * Decimal(
            settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - subtotal
    else:
        delivery = Decimal(0)
        free_delivery_delta = Decimal(0)

    grand_total = subtotal + delivery  # Add delivery cost to the grand total

    context = {
        "bag_items": bag_items,
        "subtotal": subtotal,  # Pass the subtotal to the template
        "total": total,
        "product_count": product_count,
        "delivery": delivery,
        "free_delivery_delta": free_delivery_delta,
        "free_delivery_threshold": settings.FREE_DELIVERY_THRESHOLD,
        "grand_total": grand_total,
    }

    return context
