from django.contrib import admin
from core.models.auth.user import User
from core.models.country.country import Country
from core.models.country.city import City
from core.models.auth.role import Role
from core.models.auth.verify_token import VerifyToken
from core.models.package.service import Service
from core.models.package.service_type import ServiceType


# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(VerifyToken)
class VerifyTokenAdmin(admin.ModelAdmin):
    pass


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    pass


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    pass


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    pass


@admin.register(ServiceType)
class ServiceTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "code")


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("id", "uid", "name", "is_deleted")
