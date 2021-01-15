from django.urls import path, re_path, include, reverse
from django.conf.urls import url
from django.conf import settings
from rest_framework.routers import DefaultRouter
from core.v1.views.auth.login import LoginAPIView
from core.v1.views.auth.role_view import RoleAPIView
from core.v1.views.package.service_type_view import ServiceTypeAPIView
from core.v1.views.auth.token_validation_view import TokenValidationView
from core.v1.views.package.service_view import ServiceView
from core.v1.views.utils_views.soft_delete_view import SoftDeleteAPIView
from core.v1.views.package.package_validity_view import PackageValidityView
from core.v1.views.package.package_viewset import PackageViewset
from core.v1.views.utils_views.status_change_view import StatusChangeAPIView

router = DefaultRouter()

router.register(r"services", ServiceView, 'services')
router.register(r"packages", PackageViewset, 'packages')


urlpatterns = [
    url(r"^login/", LoginAPIView.as_view()),
    url(r"^roles/", RoleAPIView.as_view()),
    url(r"^service-types/", ServiceTypeAPIView.as_view()),
    url(r"^token-validation/", TokenValidationView.as_view()),
    url(r"^generic-soft-delete/", SoftDeleteAPIView.as_view()),
    url(r"^package-validity-list/", PackageValidityView.as_view()),
    url(r"^generic-status-change/", StatusChangeAPIView.as_view()),
    re_path(r"^", include(router.urls)),
]
