from core.models.country.city import City

CITIES = ["Dhaka", "Chattogram", "Sylhet", "Rajshahi", "Cumilla", "Khulna", "Cox's Bazar", "Bogura", "Barishal", "Satkhira", "Mymensingh", "Khushtia", "Lakshmipur", "Jaipur"]
def init_cities(country):
    for city in CITIES:
        instance = City.objects.filter(country=country, name=city).first()

        if instance is None:
            instance = City.objects.create(country=country, name=city)
