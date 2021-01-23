from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters
from core.v1.permissions.is_admin_user_permission import IS_ADMIN_USER
from engine.models.associate.country import Country
from core.v1.views.generic_viewset import GenericViewset
import logging

logger = logging.getLogger(__name__)


class CountryViewset(GenericViewset):
    queryset = Country.objects.all()
    serializer_class = Country.get_serializer_class()
    permission_classes = (IsAuthenticated, IS_ADMIN_USER)