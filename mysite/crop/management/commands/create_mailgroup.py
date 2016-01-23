from django.core.management.base import BaseCommand, CommandError
from crop.models import Worker
from django.contrib.auth.models import Group

class Command(BaseCommand):
    help = 'Create mail group and refresh mailing list'

    def handle(self, *args, **options):
        # create mailing list group
        g, created = Group.objects.get_or_create(name='mailgroup', defaults={})
        # refresh
        mailing_list = ['test1',
                        'test2',
                        ]

        for person in mailing_list:
            user = Worker.objects.get(username=person)
            g.user_set.add(user)
            print 'user %s has been add to mailing list' % person
