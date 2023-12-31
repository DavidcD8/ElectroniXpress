from .models import Item, Location
from django import forms
from .models import UserProfile
from .models import Subscriber


class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email']


#User Form
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


CONDITION_CHOICES = (
    ("new", "New"),
    ("used", "Used"),
)


class ItemForm(forms.ModelForm):
    condition = forms.ChoiceField(choices=CONDITION_CHOICES, label="Condition")

    class Meta:
        model = Item
        fields = ['name', 'description', 'price', 'image', 'quantity', 'is_available', 'condition']


class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'description', 'price', 'image', 'quantity', 'is_available', 'condition']


class MarkItemAsSoldForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['is_sold']


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
