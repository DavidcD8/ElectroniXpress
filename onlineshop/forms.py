from .models import Item, Location
from django import forms

STATUS = ((0, "sold"), (1, "instock"))


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'description', 'price', 'image']


# You can Define a list of location choices
EXTRA_LOCATIONS = [
    (1, "Dublin"),
    (2, "Galway"),
    (3, "Limerick"),
    
]


class LocationForm(forms.Form):
    # This will aloow extra locations
    location_choices = [(0, "Cork")] + EXTRA_LOCATIONS

    location = forms.ChoiceField(
        choices=location_choices,
        required=False
    )
