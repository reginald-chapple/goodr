from django import forms

from causes.models import Project, Cause

class ProjectForm(forms.ModelForm):
    title = forms.CharField(max_length=255, min_length=3, strip=True, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(max_length=5000, min_length=3, strip=True, required=True, widget=forms.Textarea(attrs={'class': 'form-control'}))
    intended_impact = forms.CharField(max_length=5000, min_length=3, strip=True, required=True, widget=forms.Textarea(attrs={'class': 'form-control'}))
    beneficaries = forms.CharField(max_length=5000, min_length=3, strip=True, required=True, widget=forms.Textarea(attrs={'class': 'form-control'}))
    target_amount = forms.DecimalField(max_digits=1, decimal_places=2, required=True, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    location = forms.CharField(max_length=255, min_length=3, strip=True, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    deadline = forms.DateField(required=True, widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    cause = forms.ModelChoiceField(queryset=Cause.objects.all(), required=True, widget=forms.Select(attrs={'class': 'form-select'}))

    class Meta:
        model = Project
        fields = ("title", "description", "intended_impact", "beneficaries", "target_amount", "location", "deadline", "cause",)
