from django import forms
from .models import TrafficData

class TrafficDataForm(forms.ModelForm):
    class Meta:
        model = TrafficData
        exclude = ['timestamp'] 
