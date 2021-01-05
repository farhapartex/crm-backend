from django.db import models
from django.contrib import auth
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers
from core.models.base_abstract import BaseAbstract
from core.constants.package_validity import PackageValidity
import logging
import uuid

logger = logging.getLogger(__name__)


class PackageValidity(BaseAbstract):
    validity_type = models.CharField(max_length=100, choices=PackageValidity.choices)
    amount = models.IntegerField()

    def __str__(self):
        return str(self.id)

    def soft_delete(self):
        self.is_deleted = True
        self.save()


    @classmethod
    def get_serializer_class(cls):
        class PackageValiditySerializer(serializers.ModelSerializer):
            class Meta:
                model = cls
                fields = ("id", "validity_type", "amount", "is_active", "is_deleted", "created_at")

        return PackageValiditySerializer
