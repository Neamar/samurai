# -*- coding: utf-8 -*-
from django.db import models


class Chateau(models.Model):
	class Meta:
		verbose_name_plural = "Chateaux"
	nom = models.CharField(max_length=100)
	avatar = models.ImageField(upload_to="chateau")


class Clan(models.Model):
	nom = models.CharField(max_length=100)
	avatar = models.ImageField(upload_to="clan")

	def __unicode__(self):
		return self.nom


class Plot(models.Model):
	nom = models.CharField(max_length=100)
	description = models.TextField()

	def __unicode__(self):
		return self.nom


class Personne(models.Model):
	HOMME = 'm'
	FEMME = 'f'
	INCONNU = '?'

	SEX_CHOICES = (
		(HOMME, '♂'),
		(FEMME, '♀'),
		(INCONNU, '?')
	)

	nom = models.CharField(max_length=100)
	sexe = models.CharField(max_length=1, choices=SEX_CHOICES, default=HOMME)
	avatar = models.ImageField(upload_to="avatar")
	clan = models.ForeignKey(Clan)

	intrigue = models.PositiveSmallIntegerField(default=1)
	combat = models.PositiveSmallIntegerField(default=1)
	gestion = models.PositiveSmallIntegerField(default=1)
	diplomatie = models.PositiveSmallIntegerField(default=1)
	strategie = models.CharField(max_length=15, blank=True, null=True)

	pere = models.ForeignKey('self', related_name='+', null=True, blank=True, on_delete=models.SET_NULL)
	mere = models.ForeignKey('self', related_name='+', null=True, blank=True, on_delete=models.SET_NULL)
	femme = models.ForeignKey('self', related_name='+', null=True, blank=True, on_delete=models.SET_NULL)
	fratrie = models.PositiveSmallIntegerField(default=1)

	chateau = models.ForeignKey(Chateau, blank=True, null=True)
	suzerain = models.ForeignKey('self', related_name='+', null=True, blank=True, on_delete=models.SET_NULL)

	description = models.TextField(blank=True, null=True)
	notes = models.TextField(blank=True, null=True)
	plot = models.ForeignKey(Plot, blank=True, null=True)

	def __unicode__(self):
		return self.nom
