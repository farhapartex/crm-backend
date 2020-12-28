from django.db import models
from django.contrib import auth
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers
from core.models.base_abstract import BaseAbstract
from core.models.package.service_type import ServiceType
from core.constants.service_volume import ServiceVolumeType
import logging, uuid

logger = logging.getLogger(__name__)


class Service(BaseAbstract):
    name = models.CharField(max_length=200)
    service_type = models.ForeignKey(ServiceType, related_name='services', on_delete=models.DO_NOTHING)
    volume_type = models.CharField(max_length=100, choices=ServiceVolumeType.choices)
    volume = models.IntegerField()

    def __str__(self):
        return str(self.id)

    @classmethod
    def get_serializer_class(cls):
        class ServiceSerializer(serializers.ModelSerializer):
            class Meta:
                model = cls
                fields = ("id", "name", "service_type", "volume_type", "volume", "created_by", "created_at", "is_active")

        return ServiceSerializer
