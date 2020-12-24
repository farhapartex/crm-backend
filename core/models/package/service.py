from django.db import models
from django.contrib import auth
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from core.models.base_abstract import BaseAbstract
import logging, uuid
from core.models.package.service_type import ServiceType
from core.constants.service_volume import ServiceVolumeType

logger = logging.getLogger(__name__)

class Service(BaseAbstract):
    name = models.CharField( max_length=200)
    service_type = models.ForeignKey(ServiceType, related_name='services', on_delete=models.DO_NOTHING)
    volume_type = models.IntegerField(choices=ServiceVolumeType.choices)
    volume = models.IntegerField()

    def __str__(self):
        return str(self.id)