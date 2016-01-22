from django.core.management.base import BaseCommand, CommandError
from crop.models import *
import cPickle as pickle

class Command(BaseCommand):
    help = 'Dump the database into pickle file'

    def handle(self, *args, **options):
        print 'Generating report...'
        print '========================================================'
        print 'Number of registered users:', len(Worker.objects.all())
        print
        for worker in Worker.objects.all():
            print '--------------------------'
            print '  ID:', worker.username
            #print '  Email:', worker.email
            print '  Accomplished jobs:', len(Job.objects.filter(user=worker))
            print '  Pay:', worker.crop_job_count * 3 + worker.none_crop_job_count
            #print worker.email
        print
        print '========================================================'
        print 'Number of processed images:', len(Crop.objects.all())
        print

        count = 0
        results = []
        with open('cropping_results.pkl', 'wb') as f:
            for crop in Crop.objects.all():
                if crop.need_crop:
                    x = crop.x1
                    y = crop.y1
                    if x < 0:
                        x = 0
                    if y < 0:
                        y = 0
                    results.append((crop.img.photo_id, crop.img.url, crop.worker.username, x, y, crop.width, crop.height))
                    count += 1
                '''
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
                '''
            pickle.dump(results, f)

        print '========================================================'
        print 'Number of cropped images:', count
        print
