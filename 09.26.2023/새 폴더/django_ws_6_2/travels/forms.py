from django import forms
from .models import Travels


class TravelsForm(forms.ModelForm):
    class Meta:
        model = Travels
        fields = '__all__'
