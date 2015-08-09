# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0004_auto_20150809_1645'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lieu',
            name='population',
        ),
        migrations.RemoveField(
            model_name='perso',
            name='chargme',
        ),
        migrations.RemoveField(
            model_name='perso',
            name='religion',
        ),
        migrations.AddField(
            model_name='lieu',
            name='clan',
            field=models.ForeignKey(default=None, to='game.Clan'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='perso',
            name='charme',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='perso',
            name='age',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='perso',
            name='assurance',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='perso',
            name='clan',
            field=models.ForeignKey(blank=True, to='game.Clan', null=True),
        ),
        migrations.AlterField(
            model_name='perso',
            name='clan_origine',
            field=models.ForeignKey(related_name='+', blank=True, to='game.Clan', null=True),
        ),
        migrations.AlterField(
            model_name='perso',
            name='compassion',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='perso',
            name='culture',
            field=models.ForeignKey(blank=True, to='game.Culture', null=True),
        ),
        migrations.AlterField(
            model_name='perso',
            name='description',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='perso',
            name='education',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='perso',
            name='femme',
            field=models.ForeignKey(related_name='+', blank=True, to='game.Perso', null=True),
        ),
        migrations.AlterField(
            model_name='perso',
            name='finesse',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='perso',
            name='foi',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='perso',
            name='honneur',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='perso',
            name='influence',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='perso',
            name='loyaute',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='perso',
            name='naissance',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='perso',
            name='notes_mj',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='perso',
            name='occupation',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='perso',
            name='patience',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='perso',
            name='pere',
            field=models.ForeignKey(blank=True, to='game.Perso', null=True),
        ),
        migrations.AlterField(
            model_name='perso',
            name='position',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='perso',
            name='rang',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='perso',
            name='suite',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='perso',
            name='suzerain',
            field=models.ForeignKey(related_name='+', blank=True, to='game.Perso', null=True),
        ),
    ]
