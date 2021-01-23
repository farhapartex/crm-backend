from django.db import models
from core.models.base_abstract import BaseAbstract
from rest_framework import serializers
import logging
import uuid

logger = logging.getLogger(__name__)


class Country(BaseAbstract):
    uid = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=80)

    def __str__(self):
        return str(self.id)

    @classmethod
    def get_serializer_class(cls):
        class CountrySerializer(serializers.ModelSerializer):
            class Meta:
                model = cls
                fields = ("id", "uid", "name", "created_at",)
                read_only_fields = ("created_at",)
                lookup_field = "uid"

        return CountrySerializer

    class Meta:
        verbose_name_plural = "Countries"