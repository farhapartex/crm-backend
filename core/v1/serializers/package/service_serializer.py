from rest_framework import serializers
from core.models.package.service import Service


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ("id", "name", "volume_type", "volume")