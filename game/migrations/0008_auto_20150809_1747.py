# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0007_auto_20150809_1725'),
    ]

    operations = [
        migrations.AddField(
            model_name='perso',
            name='factions',
            field=models.ManyToManyField(related_name='+', to='game.Clan'),
        ),
        migrations.AlterField(
            model_name='clan',
            name='culture',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='clan',
            name='description',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='clan',
            name='leader',
            field=models.ForeignKey(related_name='+', blank=True, to='game.Perso', null=True),
        ),
        migrations.AlterField(
            model_name='clan',
            name='tresorerie',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='lieu',
            name='nom',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='lieu',
            name='type',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='perso',
            name='sexe',
            field=models.CharField(max_length=200, choices=[(b'homme', b'Homme'), (b'femme', b'Femme')]),
        ),
        migrations.AlterField(
            model_name='unite',
            name='commandant',
            field=models.ForeignKey(blank=True, to='game.Perso', null=True),
        ),
        migrations.AlterField(
            model_name='unite',
            name='description',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='unite',
            name='entrainement',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='unite',
            name='experience',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='unite',
            name='moral',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='unite',
            name='nombre',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='unite',
            name='position',
            field=models.ForeignKey(blank=True, to='game.Lieu', null=True),
        ),
    ]
