from .models import Item, Location
from django import forms
from .models import UserProfile

STATUS = ((0, "sold"), (1, "instock"))


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'  # Include all fields except 'user'
        exclude = ('user', 'profile_picture')  # Exclude 'user' field

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_phone_number': 'Phone Number',
            'default_postcode': 'Postal Code',
            'default_town_or_city': 'Town or City',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county': 'County, State, or Locality',
        }

        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0 profile-form-input'
            self.fields[field].label = False


class ItemForm(forms.ModelForm):
    condition = forms.ChoiceField(choices=CONDITION_CHOICES, label="Condition")

    class Meta:
        model = Item
        fields = ['name', 'description', 'price', 'image',
                  'quantity', 'is_available', 'condition']


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
