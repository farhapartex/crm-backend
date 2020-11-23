from django.contrib import admin
from core.models.auth.user import User
from core.models.country.country import Country
from core.models.country.city import City
from core.models.auth.role import Role
from core.models.auth.verify_token import VerifyToken
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
