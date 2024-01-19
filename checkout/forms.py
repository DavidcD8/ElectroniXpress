from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    country = forms.ChoiceField(
        choices=CountryField().choices + [('', 'Select Country')],
        widget=CountrySelectWidget(attrs={'class': 'custom-select d-block w-100'})
    )

    class Meta:
        model = Order
        fields = (
            "full_name",
            "email",
            "phone_number",
            "street_address1",
            "street_address2",
            "town_or_city",
            "postcode",
            "country",  # Include the country field here
            "county",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            "full_name": "Full Name",
            "email": "Email Address",
            "phone_number": "Phone Number",
            "postcode": "Postal Code",
            "town_or_city": "Town or City",
            "street_address1": "Street Address 1",
            "street_address2": "Street Address 2",
            "county": "County",
        }

        for name, field in self.fields.items():
            if name != "country":
                if field.required:
                    placeholder = f"{placeholders[name]} *"
                else:
                    placeholder = placeholders[name]
                field.widget.attrs["placeholder"] = placeholder
                field.widget.attrs["class"] = "stripe-style-input"
                field.label = False

        # Remove label for the country field
        self.fields['country'].label = False
