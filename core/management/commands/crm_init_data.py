from django.core.management.base import BaseCommand, CommandError
from core.management.commands.utils.init_country import init_country
from core.management.commands.utils.init_cities import init_cities

class Command(BaseCommand):

    def handle(self, *args, **options):
        '''init country'''
        country = init_country()

        '''init city'''
        init_cities(country)
        