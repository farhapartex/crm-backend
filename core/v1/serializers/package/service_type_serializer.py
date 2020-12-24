from rest_framework import serializers
from django.db import models
from core.models.package.service_type import ServiceType


class ServiceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceType
        fields = ("id", "name", "code")
