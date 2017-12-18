from django.contrib import admin
from login.models import AccountData, Accounts, AccountsIpauth, Gameservers


admin.site.register(Accounts)
admin.site.register(Gameservers)