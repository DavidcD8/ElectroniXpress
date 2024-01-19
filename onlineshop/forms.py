from .models import Item
from django import forms
from .models import UserProfile
from .models import Subscriber
from django_countries.fields import CountryField
from django.db import models
class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ["email"]


class UserProfileForm(forms.ModelForm):
    default_country = forms.ChoiceField(choices=CountryField().choices + [('', 'Select Country')])

    class Meta:
        model = UserProfile
        fields = "__all__"  # Include all fields except 'user'
        exclude = ("user", "profile_picture")  # Exclude 'user' field

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            "default_phone_number": "Phone Number",
            "default_postcode": "Postal Code",
            "default_town_or_city": "Town or City",
            "default_street_address1": "Street Address 1",
            "default_street_address2": "Street Address 2",
            "default_county": "County, State, or Locality",
        }

        for name, field in self.fields.items():
            if name != "default_country":
                if field.required:
                    placeholder = f"{placeholders[name]} *"
                else:
                    placeholder = placeholders[name]
                field.widget.attrs["placeholder"] = placeholder
                field.widget.attrs["class"] = "border-black rounded-0 profile-form-input"
                field.label = False

        # Remove label for the default_country field
        self.fields['default_country'].label = False
 

CONDITION_CHOICES = (
    ("new", "New"),
    ("used", "Used"),
)


class ItemForm(forms.ModelForm):
    condition = forms.ChoiceField(choices=CONDITION_CHOICES, label="Condition")

    class Meta:
        model = Item
        fields = ["name", "description", "price",
                  "image", "quantity", "condition"]


class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ["name", "description", "price",
                  "image", "quantity", "condition"]


class MarkItemAsSoldForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ["is_sold"]


class AddToCartForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, initial=1)


class CheckoutForm(forms.Form):
    billing_name = forms.CharField(max_length=255, required=True)
    billing_address = forms.CharField(max_length=255, required=True)
    card_number = forms.IntegerField(required=True)
    expiry_date = forms.IntegerField(required=True)
    cvv = forms.IntegerField(required=True)


class UpdateQuantityForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, max_value=99)
