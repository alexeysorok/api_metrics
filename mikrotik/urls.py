from rest_framework import routers
from .api import MetricViewSet


router = routers.DefaultRouter()
router.register('api/mikrotik', MetricViewSet, 'mikrotik')

urlpatterns = router.urls