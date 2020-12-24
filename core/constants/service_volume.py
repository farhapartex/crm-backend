from django.db import models
from django.utils.translation import gettext_lazy as __


class ServiceVolumeType(models.TextChoices):
    HOUR = 1, __("Hour")
    LIMIT = 2, __("Limit")
