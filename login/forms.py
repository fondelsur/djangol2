from django.forms import ModelForm
from django import forms
from login.models import Accounts


class AccountsForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Accounts
        fields = ['login', 'password', 'email']
