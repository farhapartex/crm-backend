from django_filters import rest_framework as filters
from django.db.models import Q
import logging

logger = logging.getLogger(__name__)


class ServiceFilter(filters.FilterSet):
    uid = filters.CharFilter(method="filter_by_uid")
    name = filters.CharFilter(method="filter_by_name")
    service_type_id = filters.CharFilter(method="filter_by_service_type_id")
    service_type_name = filters.CharFilter(method="filter_by_service_type_name")
    generic_search = filters.CharFilter(method="filter_by_generic_search")
    is_active = filters.BooleanFilter(method="filter_by_is_active")

    def filter_by_uid(self, queryset, name, value):
        if value is None:
            return queryset
        try:
            return queryset.filter(uid__contains=value)
        except:
            return queryset.none()

    def filter_by_name(self, queryset, name, value):
        if value is None:
            return queryset
        try:
            return queryset.filter(name__contains=value)
        except:
            return queryset.none()

    def filter_by_service_type_id(self, queryset, name, value):
        if value is None or value == "null":
            return queryset
        try:
            return queryset.filter(service_type__id=value)
        except:
            return queryset.none()

    def filter_by_service_type_name(self, queryset, name, value):
        if value is None:
            return queryset
        try:
            return queryset.filter(service_type__name__contains=value.capitalize())
        except:
            return queryset.none()

    def filter_by_generic_search(self, queryset, name, value):
        if value is None or value == "null":
            return queryset
        try:
            return queryset.filter(Q(service_type__name__contains=value.capitalize()) | Q(name__contains=value) | Q(uid__contains=value))
        except:
            return queryset.none()

    def filter_by_is_active(self, queryset, name, value):
        if value is None:
            return queryset
        try:
            return queryset.filter(is_active=value)
        except:
            return queryset.none()