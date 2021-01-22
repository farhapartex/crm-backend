from django_filters import rest_framework as filters
from django.db.models import Q
import logging

logger = logging.getLogger(__name__)


class StaffUserFilter(filters.FilterSet):
    generic_search = filters.CharFilter(method="filter_by_generic_search")

    def filter_by_generic_search(self, queryset, name, value):
        if value is None or value == "null":
            return queryset
        try:
            return queryset.filter(Q(uid__contains=value) | Q(user__username__contains=value) | Q(user__first_name__contains=value) | Q(user__last_name__contains=value) | Q(user__mobile__contains=value))
        except:
            return queryset.none()