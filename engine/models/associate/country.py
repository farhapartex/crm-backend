from django.db import models
from core.models.base_abstract import BaseAbstract
import logging
import uuid

logger = logging.getLogger(__name__)


class Country(BaseAbstract):
    name = models.CharField(max_length=80)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name_plural = "Countries"