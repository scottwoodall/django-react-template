from backend.routers import SharedAPIRootRouter

from .views import UserViewSet

router = SharedAPIRootRouter()
router.register(r'users', UserViewSet)
urlpatterns = router.urls
