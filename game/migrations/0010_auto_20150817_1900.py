# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0009_auto_20150809_1751'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Religion',
        ),
        migrations.RemoveField(
            model_name='perso',
            name='assurance',
        ),
        migrations.RemoveField(
            model_name='perso',
            name='charme',
        ),
        migrations.RemoveField(
            model_name='perso',
            name='compassion',
        ),
        migrations.RemoveField(
            model_name='perso',
            name='education',
        ),
        migrations.RemoveField(
            model_name='perso',
            name='finesse',
        ),
        migrations.RemoveField(
            model_name='perso',
            name='foi',
        ),
        migrations.RemoveField(
            model_name='perso',
            name='honneur',
        ),
        migrations.RemoveField(
            model_name='perso',
            name='influence',
        ),
        migrations.RemoveField(
            model_name='perso',
            name='loyaute',
        ),
        migrations.RemoveField(
            model_name='perso',
            name='notes_mj',
        ),
        migrations.RemoveField(
            model_name='perso',
            name='patience',
        ),
        migrations.AlterField(
            model_name='clan',
            name='culture',
            field=models.ForeignKey(related_name='+', default=None, to='game.Clan'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='clan',
            name='nom',
            field=models.CharField(unique=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='lieu',
            name='nom',
            field=models.CharField(max_length=200, unique=True, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='perso',
            name='culture',
            field=models.ForeignKey(related_name='+', blank=True, to='game.Clan', null=True),
        ),
        migrations.AlterField(
            model_name='perso',
            name='factions',
            field=models.ManyToManyField(related_name='+', to='game.Clan', blank=True),
        ),
        migrations.AlterField(
            model_name='perso',
            name='nom',
            field=models.CharField(unique=True, max_length=200),
        ),
        migrations.DeleteModel(
            name='Culture',
        ),
    ]
