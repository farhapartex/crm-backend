from django_filters import rest_framework as filters
import logging

logger = logging.getLogger(__name__)


class ServiceFilter(filters.FilterSet):
    uid = filters.CharFilter(method="filter_by_uid")

    def filter_by_uid(self, queryset, name, value):
        if value is None:
            return queryset
        try:
            return queryset.filter(uid=value)
        except:
            return queryset.none()