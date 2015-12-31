from django.core.management.base import BaseCommand, CommandError
from crop.models import *
import cPickle as pickle

class Command(BaseCommand):
    help = 'Dump the database into pickle file'

    def handle(self, *args, **options):
        with open('report.pkl', 'w') as f:
            for crop in Crop.objects.all():
                photo_id = crop.img.photo_id
                photo_url = crop.img.url
                if not crop.need_crop:
                    need_crop = False
                    data = {'photo_id': photo_id,
                            'photo_url': photo_url,
                            'need_crop': need_crop}
                    pickle.dump(data, f)
                else:
                    need_crop = True
                    x1 = crop.x1
                    y1 = crop.y1
                    width = crop.width
                    height = crop.height
                    data = {'photo_id': photo_id,
                            'photo_url': photo_url,
                            'need_crop': need_crop,
                            'x1': x1,
                            'y1': y1,
                            'width': width,
                            'height': height}
                    pickle.dump(data, f)

    
