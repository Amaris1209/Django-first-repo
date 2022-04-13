from rest_framework import routers

from .views import gari_walaCreateViewSet

router = routers.SimpleRouter()
router.register(r'gari_wala', gari_walaCreateViewSet)

urlpatterns = router.urls