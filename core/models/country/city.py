from django.db import models
from django.contrib import auth
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from core.models.base_abstract import BaseAbstract
from core.models.country.country import Country
import logging, uuid

logger = logging.getLogger(__name__)

class City(BaseAbstract):
    country = models.ForeignKey(Country, related_name='cities', on_delete=models.CASCADE)
    name = models.CharField( max_length=80)

    def __str__(self):
        return str(self.id)