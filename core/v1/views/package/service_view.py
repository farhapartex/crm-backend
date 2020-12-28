from rest_framework import status, views, viewsets
from rest_framework.permissions import IsAuthenticated
from core.v1.permissions.is_admin_user_permission import IS_ADMIN_USER
from rest_framework.response import Response
from core.models.package.service import Service


class ServiceView(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = Service.get_serializer_class()
    permission_classes = (IsAuthenticated, IS_ADMIN_USER)