# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0006_auto_20150809_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lieu',
            name='chef',
            field=models.ForeignKey(blank=True, to='game.Perso', null=True),
        ),
        migrations.AlterField(
            model_name='lieu',
            name='clan',
            field=models.ForeignKey(blank=True, to='game.Clan', null=True),
        ),
        migrations.AlterField(
            model_name='lieu',
            name='description',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='lieu',
            name='lieu',
            field=models.ForeignKey(related_name='+', blank=True, to='game.Lieu', null=True),
        ),
    ]
