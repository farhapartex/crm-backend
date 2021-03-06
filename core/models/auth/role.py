from django.db import models
from django.contrib import auth
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from core.models.base_abstract import BaseAbstract
import logging, uuid

logger = logging.getLogger(__name__)

class Role(BaseAbstract):
    name = models.CharField( max_length=50)

    def __str__(self):
        return str(self.id)

    def as_json(self):
        return {
            "id": self.id,
            "name": self.name
        }