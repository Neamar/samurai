# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0014_changes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Change',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('perso', models.ForeignKey(to='game.Perso')),
            ],
        ),
        migrations.RemoveField(
            model_name='changes',
            name='perso',
        ),
        migrations.DeleteModel(
            name='Changes',
        ),
    ]
