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
            validity_json = serializers.SerializerMethodField()
            total_service = serializers.SerializerMethodField()

            def get_validity_json(self, instance):
                return {"id": instance.validity.id, "amount": instance.validity.amount, "validity_type": instance.validity.validity_type}

            def get_total_service(self, instance):
                return instance.services.all().count()

            class Meta:
                model = cls
                fields = ("id", "uid", "name", "price", "validity", "services", "is_private", "is_active", "created_at", 'validity_json', 'total_service')
                read_only_fields = ("validity_json", "total_service")
                lookup_field = "uid"

        return PackageSerializer
