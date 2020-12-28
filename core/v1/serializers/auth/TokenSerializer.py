from django.utils.decorators import method_decorator
from rest_framework import serializers


class TokenSerializer(serializers.Serializer):
    client_id = serializers.CharField(allow_blank=False)
    client_secret = serializers.CharField(allow_blank=False)
    grant_type = serializers.CharField(allow_blank=False)
    username = serializers.CharField(allow_blank=False)
    password = serializers.CharField(allow_blank=False)
