from django import forms

from causes.models import Assignment

class AssignmentForm(forms.ModelForm):
    task = forms.CharField(max_length=255, required=True, strip=True, widget=forms.TextInput(attrs={'class': 'form-control',}))
    location = forms.CharField(max_length=255, required=True, strip=True, widget=forms.TextInput(attrs={'class': 'form-control',}))
    
    class Meta:
        model = Assignment
        fields = ("task","location",)
