from engine.models.customer.customer_base import CustomerAbstract
from django.db import models
from rest_framework import serializers
from core.models.auth.user import User
from engine.models.customer.organization import Organization
from engine.models.associate.country import Country
import uuid


class Customer(CustomerAbstract):
    uid = models.UUIDField(default=uuid.uuid4, editable=False)
    country = models.ForeignKey(Country, related_name="+", on_delete=models.DO_NOTHING)
    organization = models.ForeignKey(Organization, related_name="org_customers", on_delete=models.DO_NOTHING, blank=True, null=True)
    designation = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.id)

    def soft_delete(self):
        self.is_deleted = True
        self.save()

    @classmethod
    def get_serializer_class(cls):
        class CustomerSerializer(serializers.ModelSerializer):
            user = User.get_serializer_class()()

            class Meta:
                model = cls
                fields = ("id", "uid", "user", "nid", "present_address", "permanent_address", "organization", "designation")

        return CustomerSerializer
