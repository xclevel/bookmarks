from django.conf.urls import url
from django.contrib.auth.views import login, logout, password_change, password_change_done
from django.contrib.auth.views import logout_then_login

from account.views import dashboard

urlpatterns = [
    url(r'^login/$',login,name='login'),
    url(r'^logout/$',logout,name='logout'),
    url(r'^logout-then-login/$',logout_then_login,name='logout_then_login'),
    url(r'^$',dashboard,name='dashboard'),
    url(r'^password-change/$',password_change,name='password_change'),
    url(r'^password-change/done/$',password_change_done,name='password_change_done'),

]