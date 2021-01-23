from django.core.management.base import BaseCommand, CommandError
from engine.management.commands.utils.init_country import init_country
from engine.management.commands.utils.init_organization_type import init_organization_type


class Command(BaseCommand):

    def handle(self, *args, **options):
        '''init country'''
        country = init_country()

        '''init organization type'''
        init_organization_type()
