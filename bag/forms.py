from django import forms


class UpdateQuantityForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, max_value=99)
