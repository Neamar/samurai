# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom', models.CharField(max_length=200)),
                ('culture', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('tresorerie', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Lieu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=200)),
                ('population', models.IntegerField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Perso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom', models.CharField(max_length=200)),
                ('sexe', models.CharField(max_length=200)),
                ('age', models.CharField(max_length=200)),
                ('culture', models.CharField(max_length=200)),
                ('religion', models.CharField(max_length=200)),
                ('position', models.TextField()),
                ('occupation', models.TextField()),
                ('naissance', models.CharField(max_length=200)),
                ('rang', models.CharField(max_length=200)),
                ('loyaute', models.CharField(max_length=200)),
                ('foi', models.CharField(max_length=200)),
                ('compassion', models.CharField(max_length=200)),
                ('honneur', models.CharField(max_length=200)),
                ('influence', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('education', models.CharField(max_length=200)),
                ('chargme', models.CharField(max_length=200)),
                ('patience', models.CharField(max_length=200)),
                ('finesse', models.CharField(max_length=200)),
                ('assurance', models.CharField(max_length=200)),
                ('suite', models.TextField()),
                ('notes_mj', models.TextField()),
                ('clan', models.ForeignKey(to='game.Clan')),
                ('clan_origine', models.ForeignKey(related_name='+', to='game.Clan')),
                ('femme', models.ForeignKey(related_name='+', to='game.Perso')),
                ('pere', models.ForeignKey(to='game.Perso')),
                ('residence', models.ForeignKey(to='game.Lieu')),
                ('suzerain', models.ForeignKey(related_name='+', to='game.Perso')),
            ],
        ),
        migrations.CreateModel(
            name='Unite',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom', models.CharField(max_length=200)),
                ('nombre', models.IntegerField()),
                ('entrainement', models.IntegerField()),
                ('description', models.TextField()),
                ('experience', models.CharField(max_length=200)),
                ('moral', models.CharField(max_length=200)),
                ('commandant', models.ForeignKey(to='game.Perso')),
                ('position', models.ForeignKey(to='game.Lieu')),
            ],
        ),
        migrations.AddField(
            model_name='lieu',
            name='chef',
            field=models.ForeignKey(to='game.Perso'),
        ),
        migrations.AddField(
            model_name='clan',
            name='leader',
            field=models.ForeignKey(related_name='+', to='game.Perso'),
        ),
    ]
