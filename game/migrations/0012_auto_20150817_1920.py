# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0011_auto_20150817_1911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perso',
            name='residence',
            field=models.ForeignKey(blank=True, to='game.Lieu', null=True),
        ),
        migrations.AlterField(
            model_name='perso',
            name='sexe',
            field=models.CharField(max_length=200, choices=[(b'H', b'Homme'), (b'F', b'Femme')]),
        ),
    ]
