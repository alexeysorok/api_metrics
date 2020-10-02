from .models import MetricMikrotik
from rest_framework import viewsets, permissions
from .serializers import MetricSerializer


class MetricViewSet(viewsets.ModelViewSet):
    queryset = MetricMikrotik.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = MetricSerializer
