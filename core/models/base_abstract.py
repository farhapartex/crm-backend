from django.db import models
from django.utils.translation import ugettext_lazy as _
from core.models.base_entity import BaseEntity


class BaseAbstract(BaseEntity):
    is_active = models.BooleanField(_('active'), default=True, )

    class Meta:
        abstract = True