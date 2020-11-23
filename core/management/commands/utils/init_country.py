from core.models.country.country import Country

def init_country():
    instance = Country.objects.filter(name='Bangladesh').first()
    if instance is None:
        instance = Country.objects.create(name='Bangladesh')
    
    return instance