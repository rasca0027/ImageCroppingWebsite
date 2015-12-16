# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='slug',
            new_name='photo_id',
        ),
        migrations.AddField(
            model_name='image',
            name='category',
            field=models.CharField(default=b'none', max_length=255),
        ),
        migrations.AddField(
            model_name='image',
            name='user_id',
            field=models.CharField(default=b'', max_length=50),
        ),
    ]
