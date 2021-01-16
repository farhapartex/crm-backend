from django.db import models
from django.utils.translation import ugettext_lazy as _
from core.models.base_entity import BaseEntity
import uuid


class BaseAbstract(BaseEntity):
    is_active = models.BooleanField(_('active'), default=True, )
    is_deleted = models.BooleanField(_('Delete'), default=False, )

    def soft_delete(self):
        pass

    def change_status(self):
        self.is_active = True if self.is_active is False else False
        self.save()

    class Meta:
        abstract = True