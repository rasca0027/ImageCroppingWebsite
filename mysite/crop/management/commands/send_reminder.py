from django.core.management.base import BaseCommand, CommandError
from crop.send_mail import send_reminding_mail

class Command(BaseCommand):
    help = 'Send mail to mailgroup receipants'

    def handle(self, *args, **options):
        send_reminding_mail()
