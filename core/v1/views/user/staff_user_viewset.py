from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters
from core.v1.permissions.is_admin_user_permission import IS_ADMIN_USER
from core.models.auth.staff_user import StaffUser
from core.v1.views.generic_viewset import GenericViewset
from core.v1.filters.staff_user_filter import StaffUserFilter
import logging

logger = logging.getLogger(__name__)


class StaffUserViewset(GenericViewset):
    queryset = StaffUser.objects.all()
    serializer_class = StaffUser.get_serializer_class()
    permission_classes = (IsAuthenticated, IS_ADMIN_USER)
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = StaffUserFilter