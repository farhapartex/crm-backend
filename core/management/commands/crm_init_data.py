from django.core.management.base import BaseCommand, CommandError
from core.management.commands.utils.init_role import init_role
from core.management.commands.utils.init_package_validity import init_package_validity


class Command(BaseCommand):

    def handle(self, *args, **options):
        '''init role'''
        init_role()

        '''init package validity'''
        init_package_validity()
