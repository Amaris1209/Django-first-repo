from rest_framework import routers

from .views import insaanCreateViewSet

router = routers.SimpleRouter()
router.register(r'insaan', insaanCreateViewSet)

urlpatterns = router.urls