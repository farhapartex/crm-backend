from django.db import models
from core.models.base_abstract import BaseAbstract
from engine.models.customer.organization_type import OrganizationType
import logging

logger = logging.getLogger(__name__)


class Organization(BaseAbstract):
    name = models.CharField(max_length=200)
    type = models.ForeignKey(OrganizationType, related_name="organizations", on_delete=models.CASCADE)
    total_employee = models.IntegerField()
    address = models.TextField()

    def __str__(self):
        return str(self.id)