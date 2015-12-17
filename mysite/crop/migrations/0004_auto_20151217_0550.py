# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crop', '0003_job_pay'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='block',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='image',
            name='block_time',
            field=models.DateTimeField(null=True),
        ),
    ]
