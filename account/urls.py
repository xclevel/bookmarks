from django.conf.urls import url
from django.contrib.auth.views import login, logout, password_change, password_change_done, password_reset,password_reset_done
from django.contrib.auth.views import logout_then_login

from account.views import dashboard,register

urlpatterns = [
    url(r'^login/$',login,name='login'),
    url(r'^logout/$',logout,name='logout'),
    url(r'^logout-then-login/$',logout_then_login,name='logout_then_login'),
    url(r'^$',dashboard,name='dashboard'),
    url(r'^password-change/$',password_change,name='password_change'),
    url(r'^password-change/done/$',password_change_done,name='password_change_done'),
    url(r'^password-reset/$',password_reset,name='password_reset'),
    url(r'^password-reset/done/$',password_reset_done,name='password_reset_done')
    url(r'^register/$',register,name='register'),
]