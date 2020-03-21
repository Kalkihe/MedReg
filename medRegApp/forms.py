from django import forms
from .models import Helper
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Location


class LocationCreationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ('city', 'location')


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = (
            'email', 'phone_number', 'comment',
            'first_name', 'last_name'
        )


class HelperCreationForm(forms.ModelForm):
    class Meta:
        model = Helper
        fields = (
            'is_available', 'qualifications',
            'medical_leaving_date', 'current_occupation',
            'current_medical_occupation'
        )