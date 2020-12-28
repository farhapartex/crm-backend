from core.models.auth.role import Role

ROLES = ["Admin", "Sales", "Customer", "User"]

def init_role():
    for role in ROLES:
        instance = Role.objects.filter(name=role).first()
        if instance is None:
            instance = Role.objects.create(name=role)