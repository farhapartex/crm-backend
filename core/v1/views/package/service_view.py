from rest_framework import status, views, viewsets
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters
from core.v1.permissions.is_admin_user_permission import IS_ADMIN_USER
from rest_framework.response import Response
from core.models.package.service import Service
from core.v1.filters.service_filter import ServiceFilter
import logging

logger = logging.getLogger(__name__)


class ServiceView(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = Service.get_serializer_class()
    permission_classes = (IsAuthenticated, IS_ADMIN_USER)
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ServiceFilter

    def retrieve(self, request, *args, **kwargs):
        logger.critical(args)
        logger.critical(kwargs)
        instance = self.get_object()
        serializer_data = self.get_serializer(instance)
        return Response(serializer_data.data)