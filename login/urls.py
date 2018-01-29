from django.conf.urls import url
from django.contrib.auth import views as auth_views
from .forms import CustomAuthenticationForm
from . import views

urlpatterns = [
    url(r'^home/', views.IndexView.as_view(), name='index'),
    url(r'^register/', views.AccountCreate.as_view(), name='create'),
    url(r'^login/$', views.custom_login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
]
