from django.core.management.base import BaseCommand, CommandError
from core.management.commands.utils.init_country import init_country
from core.management.commands.utils.init_cities import init_cities
from core.management.commands.utils.init_role import init_role
from core.management.commands.utils.init_package_validity import init_package_validity


class Command(BaseCommand):

    def handle(self, *args, **options):
        '''init role'''
        init_role()

        '''init country'''
        country = init_country()

        '''init city'''
        init_cities(country)

        '''init package validity'''
        init_package_validity()
