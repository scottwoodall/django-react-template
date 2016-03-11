from django.conf import settings
from django.conf.urls import url, include
from django.contrib.auth.views import login
from django.contrib import admin

from backend.routers import SharedAPIRootRouter

from .views import app, index

"""
http://stackoverflow.com/questions/20825029/registering-api-in-apps#22684199
"""


def api_urls():
    from importlib import import_module
    for app in settings.LOCAL_APPS:
        try:
            import_module(app + '.urls')
        except (ImportError, AttributeError):
            pass
    return SharedAPIRootRouter.shared_router.urls


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(api_urls())),
    url(r'^app/', app, name='app'),
    url('^auth/login/$', login, name='login'),
    url('^$', index, name='index'),
]
