from django.db import models
from core.models.base_abstract import BaseAbstract
import logging
import uuid

logger = logging.getLogger(__name__)


class CustomerAbstract(BaseAbstract):
    user = models.ForeignKey("core.User", related_name="customers", on_delete=models.CASCADE)
    nid = models.CharField(max_length=20)
    present_address = models.TextField()
    permanent_address = models.TextField()

    class Meta:
        abstract = True