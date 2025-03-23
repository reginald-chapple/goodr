from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from users.models import User

class CreateUserForm(UserCreationForm):
    username = forms.CharField(min_length=1, max_length=30, required=True, strip=True, widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'User name'}))
    name = forms.CharField(min_length=1, max_length=60, required=True, strip=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}))
    email = forms.CharField(min_length=1, max_length=60, required=True, strip=True, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email', 'autofocus': False }))
    photo = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(min_length=1, max_length=60, required=True, strip=True, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2 = forms.CharField(min_length=1, max_length=60, required=True, strip=True, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}))
    
    class Meta(UserCreationForm):
        model = User
        fields = ('username', 'name', 'email', 'photo',)

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_member = True
        user.save()
        # Member.objects.create(user=user)
        return user
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'autofocus': False})

class UserForm(forms.ModelForm):
    email = forms.CharField(min_length=1, max_length=60, required=False, strip=True, widget=forms.EmailInput(attrs={'class': 'form-control','placeholder': 'Email' }))
    name = forms.CharField(min_length=1, max_length=60, required=False, strip=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}))
    photo = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}))
    phone_number = forms.CharField(min_length=16, max_length=16, required=False, strip=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone number'}))
    birthdate = forms.DateField(required=False, widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Birth date', 'type': 'date'}))
    
    class Meta:
        model = User
        fields = ('name', 'email', 'photo', 'phone_number', 'birthdate',)