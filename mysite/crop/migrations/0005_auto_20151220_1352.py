# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('crop', '0004_auto_20151217_0550'),
    ]

    operations = [
        migrations.CreateModel(
            name='Crop',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('need_crop', models.BooleanField(default=True)),
                ('x1', models.IntegerField(null=True)),
                ('y1', models.IntegerField(null=True)),
                ('width', models.IntegerField(null=True)),
                ('height', models.IntegerField(null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='image',
            name='crops',
        ),
        migrations.AlterField(
            model_name='job',
            name='pay',
            field=models.FloatField(default=b'3'),
        ),
        migrations.AddField(
            model_name='crop',
            name='img',
            field=models.ForeignKey(to='crop.Image'),
        ),
        migrations.AddField(
            model_name='crop',
            name='worker',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
