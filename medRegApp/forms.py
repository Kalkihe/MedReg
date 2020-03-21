from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import (CustomUser, Helper, HelpRequest, HelpSeeker, Institution,
                     Location)


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
        widgets = {
            'medical_leaving_date': forms.DateInput(
                attrs={'class': 'mld'}
            ),
        }

    class Media:
        css = {'all': ('datepicker.min.css',)}
        js = ('datepicker.min.js', 'dp_helper.js')


class HelpSeekerCreationForm(forms.ModelForm):
    class Meta:
        model = HelpSeeker
        fields = ('institution',)


class InstituionCreationForm(forms.ModelForm):
    class Meta:
        model = Institution
        fields = ('name', 'comment')


class HelpRequestCreationForm(forms.ModelForm):
    class Meta:
        model = HelpRequest
        fields = (
            'description', 'start_date', 'end_date',
            'required_helper_count'
        )
        widgets = {
            'start_date': forms.DateInput(
                attrs={'class': 'dp_start'}
            ),
            'end_date': forms.DateInput(
                attrs={'class': 'dp_end'}
            )
        }

    class Media:
        css = {'all': ('datepicker.min.css',)}
        js = ('datepicker.min.js', 'dp_helprequest.js')
