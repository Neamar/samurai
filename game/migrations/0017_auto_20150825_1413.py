# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0016_auto_20150824_1917'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clan',
            name='tresorerie',
        ),
        migrations.AlterField(
            model_name='clan',
            name='militaire',
            field=models.IntegerField(default=0),
        ),
    ]
