from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^success/', views.IndexView.as_view(), name='index'),
    url(r'^$', views.AccountCreate.as_view(), name='create'),

]
