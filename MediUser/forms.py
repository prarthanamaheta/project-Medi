from django.contrib.auth.forms import UserCreationForm

from django import forms

from MediDonor.models import Organ
from MediUser.models import MediUser


class SignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = MediUser
        fields = ('username', 'email', 'mobile')


class LogingForm(forms.Form):
    class Meta:
        model = MediUser
        username = forms.CharField(max_length=69)
        password = forms.CharField(widget=forms.PasswordInput)


class DonateForm(forms.Form):
    class Meta:
        model = Organ


class EditDonateForm(forms.Form):
    class Meta:
        model = Organ
        fields = '__all__'


class PasswordChangeForm(forms.Form):
    class Meta:
        model = MediUser
        fields = ['password']
