# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_auto_20150804_1418'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lieu',
            options={'verbose_name_plural': 'lieux'},
        ),
        migrations.AddField(
            model_name='lieu',
            name='lieu',
            field=models.ForeignKey(related_name='+', default=None, to='game.Lieu'),
            preserve_default=False,
        ),
    ]
