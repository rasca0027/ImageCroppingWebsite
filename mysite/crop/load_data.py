from django.core.management.base import BaseCommand, CommandError
from crop.import_data import load_data

class Command(BaseCommand):
    help = 'Check and load new data'

    def handle(self, *args, **options):
        load_data()
