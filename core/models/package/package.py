from django.db import models
from django.contrib import auth
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers
from core.models.package.package_abstract import PackageBaseAbstract


class Package(PackageBaseAbstract):
    is_private = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)

    def soft_delete(self):
        self.is_deleted = True
        self.save()


    @classmethod
    def get_serializer_class(cls):
        class PackageSerializer(serializers.ModelSerializer):
            class Meta:
                model = cls
                fields = ("id", "uid", "name", "validity", "services", "is_active", "created_at")

        return PackageSerializer
