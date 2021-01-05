from django.db import models
from django.utils.translation import gettext_lazy as __


class PackageValidity(models.TextChoices):
    MONTH = "MONTH", __("Month")
    YEAR = "YEAR", __("Year")
    DAY = "DAY", __("Day")