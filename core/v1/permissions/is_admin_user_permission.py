from django.contrib.auth.models import Group, Permission
from rest_framework import permissions
from core.models.auth.user import User
import logging

class IS_ADMIN_USER(permissions.BasePermission):

    def has_permission(self, request, view):
        user = request.user
        return user.is_admin_user()