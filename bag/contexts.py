from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from onlineshop.models import Item  # Adjust model import if needed

def bag_contents(request):
    bag_items = []
    total = 0
    bag_total_quantity = 0  # Renamed from product_count for clarity
    bag = request.session.get("bag", {})

    for item_id, quantity in bag.items():
        item = get_object_or_404(Item, pk=item_id)
        total += item.price * quantity
        bag_total_quantity += quantity  # Count total quantity of items
        bag_items.append(
            {
                "item_id": item_id,
                "quantity": quantity,
                "item": item,
                "total_price": item.price * quantity,
            }
        )

    subtotal = total

    # Delivery cost logic
    if subtotal < settings.FREE_DELIVERY_THRESHOLD:
        delivery = subtotal * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - subtotal
    else:
        delivery = Decimal(0)
        free_delivery_delta = Decimal(0)

    grand_total = subtotal + delivery  

    context = {
        "bag_items": bag_items,
        "subtotal": subtotal,
        "total": total,
        "bag_total_quantity": bag_total_quantity,  # ✅ Pass this to the template
        "delivery": delivery,
        "free_delivery_delta": free_delivery_delta,
        "free_delivery_threshold": settings.FREE_DELIVERY_THRESHOLD,
        "grand_total": grand_total,
    }

    return context
