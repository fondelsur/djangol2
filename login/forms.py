from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import AuthenticationForm

from login.models import Accounts


class AccountsForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Accounts
        fields = ['login', 'password', 'email']


class CustomAuthenticationForm(AuthenticationForm):
    """
    Custom authentication form for access.
    """
    def confirm_login_allowed(self, user):
        if not user.is_active or not user.is_validated:
            raise forms.ValidationError(
                'There was a problem with your login.',
                code='invalid_login'
                        )
