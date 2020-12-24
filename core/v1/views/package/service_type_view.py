from django.db import models
from rest_framework import status, views, viewsets
from rest_framework.permissions import IsAuthenticated
from core.v1.permissions.is_admin_user_permission import IS_ADMIN_USER
from rest_framework.response import Response
from core.models.package.service_type import ServiceType
from core.v1.serializers.package.service_type_serializer import ServiceTypeSerializer


class ServiceTypeAPIView(views.APIView):
    permission_classes = (IsAuthenticated, IS_ADMIN_USER,)

    def get(self, request, *args, **kwargs):
        queryset = ServiceType.objects.all()
        serializer_data = ServiceTypeSerializer(queryset, many=True).data
        return Response(data={"data": serializer_data, "success": True}, status=status.HTTP_200_OK)
