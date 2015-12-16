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
    crops = models.TextField(blank=True)

    def __unicode__(self):
        return self.photo_id


class Job(models.Model):

    title = models.CharField(max_length=255, blank=True)
    done = models.BooleanField(default=False)
    user = models.ForeignKey(Worker, blank=True)
    image = models.ManyToManyField(Image, null=False)

    def __unicode__(self):
        return self.title

