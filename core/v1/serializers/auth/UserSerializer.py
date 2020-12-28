from rest_framework import serializers
from core.models.auth.user import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
