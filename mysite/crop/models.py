from django.db import models
from django.contrib.auth.models import AbstractUser

class Worker(AbstractUser):
    
    money = models.FloatField(default=0)
    
    def __unicode__(self):
        return self.username


class Image(models.Model):
    count = models.PositiveSmallIntegerField(default=0)
    photo_id = models.SlugField()
    user_id = models.CharField(max_length=50, default='')
    category = models.CharField(max_length=255, default='none')
    url = models.URLField()
    block = models.BooleanField(default=False)
    block_time = models.DateTimeField(null=True)

    def __unicode__(self):
        return self.photo_id


class Crop(models.Model):
    img = models.ForeignKey(Image)
    worker = models.ForeignKey(Worker)
    need_crop = models.BooleanField(default=True)
    x1 = models.IntegerField(null=True) 
    y1 = models.IntegerField(null=True)
    width = models.IntegerField(null=True)
    height = models.IntegerField(null=True)

    def __unicode__(self):
        return self.img.photo_id


class Job(models.Model):

    title = models.CharField(max_length=255, blank=True)
    done = models.BooleanField(default=False)
    user = models.ForeignKey(Worker, blank=True)
    image = models.ManyToManyField(Image, null=False)
    pay = models.FloatField(default='3')

    def __unicode__(self):
        return self.title

