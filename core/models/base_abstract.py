from django.db import models
from django.utils.translation import ugettext_lazy as _
from core.models.base_entity import BaseEntity
import uuid


class BaseAbstract(BaseEntity):
    is_active = models.BooleanField(_('active'), default=True, )
    is_deleted = models.BooleanField(_('Delete'), default=False, )

    def soft_delete(self):
        pass

    class Meta:
        abstract = True