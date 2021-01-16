from rest_framework import serializers


class StatusChangeSerializer(serializers.Serializer):
    uid = serializers.CharField(max_length=500)
    context = serializers.CharField(max_length=500)
