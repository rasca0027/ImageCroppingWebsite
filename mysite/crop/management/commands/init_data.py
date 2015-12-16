from django.core.management.base import BaseCommand, CommandError
from crop.import_data import init_data

class Command(BaseCommand):
    help = 'Generate event from meetup'

    def handle(self, *args, **options):
        init_data()
