from django import forms

from causes.models import Objective

class ObjectiveForm(forms.ModelForm):
    description = forms.CharField(max_length=255, min_length=3, strip=True, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    target_value = forms.DecimalField(required=True, max_digits=10, decimal_places=2, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    unit_of_measurement = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = Objective
        fields = ("description","target_value","unit_of_measurement",)
