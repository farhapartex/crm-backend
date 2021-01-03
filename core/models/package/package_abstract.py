from django.db import models
from django.utils.translation import ugettext_lazy as _
from core.models.base_abstract import BaseAbstract
from core.models.package.service import Service
from core.models.package.validity import PackageValidity
import logging
import uuid

logger = logging.getLogger(__name__)


class PackageBaseAbstract(BaseAbstract):
    name = models.CharField(max_length=500)
    validity = models.ForeignKey(PackageValidity, related_name="packages", on_delete=models.CASCADE)
    services = models.ManyToManyField(Service)
    price = models.IntegerField(default=0)
    uid = models.UUIDField(default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True
