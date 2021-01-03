from rest_framework import status, views
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters
from core.v1.permissions.is_admin_user_permission import IS_ADMIN_USER
from rest_framework.response import Response
from core.v1.views.generic_view import GenericAPIView
from core.models.package.validity import PackageValidity
import logging

logger = logging.getLogger(__name__)


class PackageValidityView(GenericAPIView):
    queryset = PackageValidity.objects.all()
    serializer_class = PackageValidity.get_serializer_class()
    permission_classes = (IsAuthenticated, IS_ADMIN_USER)
    pagination_class = None
