from django.conf.urls import url, include
from django.contrib.auth import login
from django.contrib.auth.views import logout_then_login
from django.contrib import admin

from .views import app, index

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('users.urls')),
    url(r'^app/', app, name='app'),
    url('^auth/login/$', login, name='login'),
    url('^auth/logout/$', logout_then_login, name='logout'),
    url('^$', index, name='index'),
]
