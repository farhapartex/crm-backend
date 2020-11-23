from django.urls import path, re_path, include, reverse
from django.conf.urls import url
from django.conf import settings
from rest_framework.routers import DefaultRouter
from core.v1.views.auth.login import LoginAPIView

router = DefaultRouter()

urlpatterns = [
    url(r"^login/", LoginAPIView.as_view()),
]
