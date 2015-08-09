# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0005_auto_20150809_1710'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perso',
            name='suite',
        ),
        migrations.AddField(
            model_name='perso',
            name='secret_1',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='perso',
            name='secret_2',
            field=models.TextField(null=True, blank=True),
        ),
    ]
