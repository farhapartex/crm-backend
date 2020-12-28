from django.db import models
from django.utils.translation import gettext_lazy as __


class ServiceVolumeType(models.TextChoices):
    HOUR = "HOUR", __("Hour")
    LIMIT = "LIMIT", __("Limit")
