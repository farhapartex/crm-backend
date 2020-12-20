from django.db import models
from django.contrib import auth
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser,UserManager, Group,_user_get_permissions, _user_has_perm, _user_has_module_perms
from django.contrib.auth.validators import UnicodeUsernameValidator
from core.models.base_abstract import BaseAbstract
from core.models.auth.role import Role
from core.models.country.country import Country
import logging, uuid

logger = logging.getLogger(__name__)

class PermissionsMixin(models.Model):
    is_superuser = models.BooleanField(
        _('superuser status'),
        default=False,
        help_text=_(
            'Designates that this user has all permissions without '
            'explicitly assigning them.'
        ),
    )
    role = models.OneToOneField(Role, related_name='role_of', null=True, on_delete=models.CASCADE)

    def get_user_permissions(self, obj=None):
        return _user_get_permissions(self, obj, 'user')

    def get_group_permissions(self, obj=None):
        return _user_get_permissions(self, obj, 'role')

    def get_all_permissions(self, obj=None):
        return _user_get_permissions(self, obj, 'all')

    def has_perm(self, perm, obj=None):
        # Active superusers have all permissions.
        if self.is_active and self.is_superuser:
            return True

        # Otherwise we need to check the backends.
        return _user_has_perm(self, perm, obj)

    def has_perms(self, perm_list, obj=None):
        return all(self.has_perm(perm, obj) for perm in perm_list)

    def has_module_perms(self, app_label):
        # Active superusers have all permissions.
        if self.is_active and self.is_superuser:
            return True

        return _user_has_module_perms(self, app_label)

    class Meta:
        abstract = True


class UserAbstract(AbstractBaseUser, PermissionsMixin, BaseAbstract):
    username_validator = UnicodeUsernameValidator()

    first_name = models.CharField(_('first name'), max_length=150)
    last_name = models.CharField(_('last name'), max_length=150)
    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    email = models.EmailField(_('email address'), unique=True)
    mobile = models.CharField(_('Mobile'), max_length=15)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta:
        abstract = True
    

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def as_json(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "username": self.username,
            "mobile": self.mobile,
            "role": self.role.name if self.role else ""
        }

    def is_admin_user(self):
        try:
            return self.role.name == "Admin"
        except:
            return False

    def is_customer_user(self):
        try:
            return self.role.name == "Customer"
        except:
            return False

    def is_sales_user(self):
        try:
            return self.role.name == "Sales"
        except:
            return False


class User(UserAbstract):
    country = models.ForeignKey(Country, related_name='users', on_delete=models.CASCADE, blank=True, null=True)

    @classmethod
    def get_instance(cls, filter_data):
        return cls.objects.filter(**filter_data).first()
        

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')