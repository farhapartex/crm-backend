from django.db import models
from django.contrib import auth
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from core.models.base_abstract import BaseAbstract
import logging, uuid

logger = logging.getLogger(__name__)


class ServiceType(BaseAbstract):
    name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.id)
