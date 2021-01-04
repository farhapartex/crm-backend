from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters
from core.v1.permissions.is_admin_user_permission import IS_ADMIN_USER
from core.v1.views.generic_viewset import GenericViewset
from core.models.package.package import Package
from core.v1.filters.package_filter import PackageFilter
import logging

logger = logging.getLogger(__name__)


class PackageViewset(GenericViewset):
    queryset = Package.objects.all()
    serializer_class = Package.get_serializer_class()
    permission_classes = (IsAuthenticated, IS_ADMIN_USER)
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = PackageFilter