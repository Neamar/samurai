# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0010_auto_20150817_1900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clan',
            name='culture',
            field=models.ForeignKey(related_name='+', blank=True, to='game.Clan', null=True),
        ),
    ]
