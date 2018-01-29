# -*- coding: utf-8 -*-

from django.urls import reverse
from django.contrib import messages
from django.views import generic
from django.contrib.auth.models import User
from django.views.generic.edit import FormView
from login.models import Accounts, Profile
from login.forms import AccountsForm, CustomAuthenticationForm
from .utils import get_top_level_players, get_top_pk_players, encrypt_l2_password
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
import base64
import hashlib


def custom_login(request):
    username = request.POST['username']
    password = request.POST['password']
    
    # We will rescue the user within the account system of L2 Server.
    try:
        encrypted_password = encrypt_l2_password(password)
        attempt = Accounts.objects.get(login=username, password=encrypted_password)
    except Accounts.DoesNotExist as e:
        return redirect(reverse('index'))
    if attempt:
        #TODO: Think something when user exists two ways.
        django_user, new = User.objects.get_or_create(username=username, password=password)
        if new:
            django_user.profile.accounts = attempt
            django_user.save()
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect(reverse('index'))
    # else:


class AccountCreate(FormView):
    form_class = AccountsForm
    success_url = '/home'
    template_name = 'login/accounts_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        old_password = self.object.password
        new_password = encrypt_l2_password(old_password)
        self.object.password = new_password
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
        context['login_form'] = CustomAuthenticationForm()
        return context
    
