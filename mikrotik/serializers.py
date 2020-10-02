from rest_framework import serializers
from .models import MetricMikrotik


class MetricSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetricMikrotik
        fields = '__all__'
