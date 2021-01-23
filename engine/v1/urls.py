from django.urls import path, re_path, include, reverse
from django.conf.urls import url
from django.conf import settings
from rest_framework.routers import DefaultRouter
from engine.v1.views.country_viewset import CountryViewset

router = DefaultRouter()

router.register(r"countries", CountryViewset, 'country_viewset')

urlpatterns = [
    # url(r"^login/", LoginAPIView.as_view()),
    re_path(r"^", include(router.urls)),
]
