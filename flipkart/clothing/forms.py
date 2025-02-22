from django import forms
from.models import dress

class dressForm(forms.ModelForm):
    class Meta:
        model = dress
        fields = ['name','size','colour','price','image']