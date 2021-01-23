from engine.models.customer.organization_type import OrganizationType

TYPES = ["Accounts & Finance", "Bank/ Insurance / Leasing", "Cargo/Freight Forwarding",
         "Design / Creative", "Electrician / Construction",
         "Housing & Real Estate", "Law / Legal", "NGO / Developments",
         "Research / Consultancy"]


def init_organization_type():
    for type in TYPES:
        instance = OrganizationType.objects.filter(name=type).first()
        if instance is None:
            instance = OrganizationType.objects.create(name=type)
