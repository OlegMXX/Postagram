from rest_framework import routers

from core.auth.viewsets import RegisterViewSet
from core.user.viewsets import UserViewSet

router = routers.SimpleRouter()


# AUTH
router.register(r'auth/register', RegisterViewSet, basename='auth-register')
# USER
router.register(r'user', UserViewSet, basename='user')

urlpatterns = [
    *router.urls,
]




