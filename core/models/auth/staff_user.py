from django.db import models
from core.models.auth.user import User
from core.models.base_abstract import BaseAbstract
from rest_framework import serializers, status
import uuid
import logging

logger = logging.getLogger(__name__)


class StaffUser(BaseAbstract):
    uid = models.UUIDField(default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, related_name='staff_users', on_delete=models.CASCADE)
    position = models.CharField(max_length=300)

    def __str__(self):
        return str(self.id)

    @classmethod
    def get_serializer_class(cls):
        class StaffUserSerializer(serializers.ModelSerializer):
            user = User.get_serializer_class()(required=False)

            def create(self, validated_data):
                try:
                    user = validated_data.pop("user")
                    user["username"] = user["email"]
                    user_instance = User.create_instance(user)
                    validated_data["user"] = user_instance
                    if user_instance is None:
                        raise serializers.ValidationError({"error": "User not found"},
                                                          status_code=status.HTTP_400_BAD_REQUEST)
                    instance = cls.objects.create(**validated_data)
                    return instance
                except:
                    raise serializers.ValidationError({"error": "Internal server error"},
                                                      status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

            def update(self, instance, validated_data):
                try:
                    user_data = validated_data.pop("user")
                    logger.critical(user_data)
                    instance.position = validated_data.get("position", instance.position)
                    instance.save()
                    # user_instance = instance.user
                    # UserSerializer = User.get_serializer_class()
                    # user_instance = instance.user
                    # user_instance.first_name = user["first_name"]
                    # user_instance.last_name = user["last_name"]
                    # user_instance.email = user["email"]
                    # user_instance.is_active = user["is_active"]
                    # user_instance.role = user["role"]
                    # user_instance.save()
                    # user_serializer = UserSerializer(data=user_data)
                    # user_serializer.update(user_instance, user_data)
                    # if user_serializer.is_valid():
                    #     user_serializer.update(user_instance, user_data)

                    return instance
                except:
                    raise serializers.ValidationError({"error": "Internal server error"},
                                                      status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

            class Meta:
                model = cls
                fields = ("id", "uid", "user", "position")
                lookup_field = "uid"

        return StaffUserSerializer
