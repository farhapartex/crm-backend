from core.models.package.validity import PackageValidity

VALIDITY_DICT = {10: "DAY", 3: "MONTH", 6: "MONTH", 1: "YEAR"}


def init_package_validity():
    for key in VALIDITY_DICT:
        query = PackageValidity.objects.filter(amount=key, validity_type=VALIDITY_DICT[key]).first()
        if query is None:
            instance = PackageValidity.objects.create(amount=key, validity_type=VALIDITY_DICT[key])
