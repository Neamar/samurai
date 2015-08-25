# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0015_auto_20150821_1031'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perso',
            name='secret_1',
        ),
        migrations.RemoveField(
            model_name='perso',
            name='secret_2',
        ),
        migrations.AddField(
            model_name='clan',
            name='militaire',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='clan',
            name='richesse',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
