from django import forms
from multiupload.fields import MultiFileField
from .models import Bike

class BikeForm(forms.ModelForm):
    class Meta:
        model = Bike
        fields = '__all__'

    purchase_date = forms.DateField(
        required=True,
        input_formats=['%Y-%m-%d'],
        widget=forms.DateInput(attrs={'type': 'date'})
    )