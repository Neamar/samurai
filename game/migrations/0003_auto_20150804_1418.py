# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_auto_20150804_1417'),
    ]

    operations = [
        migrations.CreateModel(
            name='Culture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Religion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='perso',
            name='culture',
            field=models.ForeignKey(to='game.Culture'),
        ),
        migrations.AlterField(
            model_name='perso',
            name='religion',
            field=models.ForeignKey(to='game.Religion'),
        ),
    ]
