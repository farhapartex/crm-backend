from django.db import models
from core.models.base_abstract import BaseAbstract
import logging

logger = logging.getLogger(__name__)


class OrganizationType(BaseAbstract):
    name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.id)