# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0012_auto_20150817_1920'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='clan',
            options={'ordering': ['nom']},
        ),
        migrations.AlterModelOptions(
            name='lieu',
            options={'ordering': ['nom'], 'verbose_name_plural': 'lieux'},
        ),
        migrations.AlterModelOptions(
            name='perso',
            options={'ordering': ['nom']},
        ),
        migrations.AddField(
            model_name='lieu',
            name='image_large',
            field=models.ImageField(null=True, upload_to=b'', blank=True),
        ),
    ]
