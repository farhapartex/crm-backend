from django.db import models
from django.utils import timezone
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from core.utils import *


class BaseEntity(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, editable=False,
                                   related_name="%(app_label)s_%(class)s_created", on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, editable=False,
                                   related_name="%(app_label)s_%(class)s_updated", on_delete=models.CASCADE)
    

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and user.is_authenticated:
            self.updated_by = user
            if self._state.adding:
                self.created_by = user
        super(BaseEntity, self).save(*args, **kwargs)

    class Meta:
        abstract = True