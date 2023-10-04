from django import forms
from .models import Travels


class TravelsForm(forms.ModelForm):
    location = forms.CharField(
        widget=forms.TextInput(
            attrs={
<<<<<<< HEAD
                'placeholder':'Enter the location'
=======
                'placeholder':'ex.제주도'
>>>>>>> 510a74c785e16d49a12e32747548ae559fbd3fea
            }
        )
    )
    start_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'placeholder':'ex.2022-02-22'
            }
        )
    )
    end_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'placeholder':'ex.2022-02-22'
            }
        )
    )

    

    
    class Meta:
        model = Travels
        fields = '__all__'
