from django import forms
from .models import Travels


class TravelsForm(forms.ModelForm):
    location = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholdeer':'Enter the location'
            }
        )
    )
    class Meta:
        model = Travels
        fields = '__all__'
