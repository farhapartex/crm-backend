from django_filters import rest_framework as filters
from django.db.models import Q
import logging

logger = logging.getLogger(__name__)


class PackageFilter(filters.FilterSet):
    generic_search = filters.CharFilter(method="filter_by_generic_search")

    def filter_by_generic_search(self, queryset, name, value):
        if value is None or value == "null":
            return queryset
        try:
            return queryset.filter(Q(name__contains=value) | Q(uid__contains=value))
        except:
            return queryset.none()