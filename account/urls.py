from django.conf.urls import url
from django.contrib.auth.views import login, logout
from django.contrib.auth.views import logout_then_login

from account.views import dashboard

urlpatterns = [
    url(r'^login/$',login,name='login'),
    url(r'^logout/$',logout,name='logout'),
    url(r'^logout-then-login/$',logout_then_login,name='logout_then_login'),
    url(r'^$',dashboard,name='dashboard'),
]