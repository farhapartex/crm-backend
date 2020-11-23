from django.db import models
from django.contrib import auth
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from core.models.base_abstract import BaseAbstract
from core.models.auth.user import User
import logging, uuid

logger = logging.getLogger(__name__)

class VerifyToken(BaseAbstract):
    user = models.ForeignKey(User, related_name='verify_tokens', on_delete=models.CASCADE)
    token = models.CharField(max_length=100)
    expire_in = models.CharField(max_length=10)

    def __str__(self):
        return str(self.id)
    
    @classmethod
    def get_instance(cls, filter_data):
        return cls.objects.filter(**filter_data).first()