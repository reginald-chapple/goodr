from django import forms

from causes.models import Project, Cause

class ProjectForm(forms.ModelForm):
    title = forms.CharField(max_length=255, min_length=3, strip=True, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    problem = forms.CharField(max_length=5000, min_length=3, strip=True, required=True, widget=forms.Textarea(attrs={'class': 'form-control'}))
    solution = forms.CharField(max_length=5000, min_length=3, strip=True, required=True, widget=forms.Textarea(attrs={'class': 'form-control'}))
    intended_impact = forms.CharField(max_length=5000, min_length=3, strip=True, required=True, widget=forms.Textarea(attrs={'class': 'form-control'}))
    beneficaries = forms.CharField(max_length=5000, min_length=3, strip=True, required=True, widget=forms.Textarea(attrs={'class': 'form-control'}))
    location = forms.CharField(max_length=255, min_length=3, strip=True, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    cause = forms.ModelChoiceField(queryset=Cause.objects.all(), required=True, widget=forms.Select(attrs={'class': 'form-select'}))

    class Meta:
        model = Project
        fields = ("title", "problem", "solution", "intended_impact", "beneficaries", "location", "cause",)
