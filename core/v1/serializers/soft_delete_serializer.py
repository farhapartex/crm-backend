from rest_framework import serializers


class SoftDeleteSerializer(serializers.Serializer):
    uid = serializers.CharField(max_length=500)
    context = serializers.CharField(max_length=500)
