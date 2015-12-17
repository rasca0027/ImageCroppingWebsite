# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crop', '0002_auto_20151216_1755'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='pay',
            field=models.FloatField(default=b'0.25'),
        ),
    ]
