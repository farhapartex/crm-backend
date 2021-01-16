from django.db import models
from django.utils.translation import gettext_lazy as __


class GenderChoice(models.TextChoices):
    MALE = "MALE", __("Male")
    FEMALE = "FEMALE", __("Female")
    OTHER = "OTHER", __("Other")