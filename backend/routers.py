from rest_framework.routers import DefaultRouter, SimpleRouter

"""
One shared router all apps can register.
This results in one api-root containing all apps.
"""


class SharedAPIRootRouter(SimpleRouter):
    shared_router = DefaultRouter(trailing_slash=True)

    def register(self, *args, **kwargs):
        self.shared_router.register(*args, **kwargs)
        super().register(*args, **kwargs)
