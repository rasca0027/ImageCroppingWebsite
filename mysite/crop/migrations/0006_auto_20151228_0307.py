# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crop', '0005_auto_20151220_1352'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='end_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='start_time',
            field=models.DateTimeField(null=True),
        ),
    ]
