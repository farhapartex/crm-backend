from django.contrib import admin
from engine.models.associate.country import Country
from engine.models.customer.customer import Customer
from engine.models.customer.organization import Organization
from engine.models.customer.organization_type import OrganizationType


# Register your models here.

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created_at")


@admin.register(OrganizationType)
class OrganizationTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created_at")


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "type", "total_employee", "is_active", "created_at")
