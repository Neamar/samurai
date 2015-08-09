# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0008_auto_20150809_1747'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='unite',
            name='commandant',
        ),
        migrations.RemoveField(
            model_name='unite',
            name='position',
        ),
        migrations.AlterField(
            model_name='perso',
            name='factions',
            field=models.ManyToManyField(related_name='+', null=True, to='game.Clan'),
        ),
        migrations.DeleteModel(
            name='Unite',
        ),
    ]
