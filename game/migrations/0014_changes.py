# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0013_auto_20150819_1919'),
    ]

    operations = [
        migrations.CreateModel(
            name='Changes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.TextField()),
                ('perso', models.ForeignKey(to='game.Perso')),
            ],
        ),
    ]
