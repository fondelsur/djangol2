# -*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.views import generic
from django.views.generic.edit import FormView
from login.models import Accounts
from login.forms import AccountsForm
from .utils import get_top_level_players, get_top_pk_players
import base64
import hashlib


class AccountCreate(FormView):
    form_class = AccountsForm
    success_url = '/home'
    template_name = 'login/accounts_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        old_password = self.object.password
        first_encoding = hashlib.sha1(old_password).digest()
        encryption = base64.b64encode(first_encoding)
        self.object.password = encryption
        self.object.save()
        messages.success(self.request, '¡Tu cuenta ha sido creada! Ya puedes jugar.')
        return super(AccountCreate, self).form_valid(form)


class IndexView(generic.ListView):
    template_name = 'login/main_template.html'
    context_object_name = 'accounts'

    def get_queryset(self):
        return Accounts.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['top_players'] = get_top_level_players()
        context['top_pk'] = get_top_pk_players()
        return context
    
