from django.forms import ModelForm
from login.models import Accounts


class AccountsForm(ModelForm):
    class Meta:
        model = Accounts
        fields = ['login', 'password', 'email']
