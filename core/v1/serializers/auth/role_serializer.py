from django.utils.decorators import method_decorator
from rest_framework import serializers
from core.models.auth.role import Role


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ("id", "name")
