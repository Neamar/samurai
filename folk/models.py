from django.db import models


class Chateau(models.Model):
	nom = models.CharField(max_length=100)


class Clan(models.Model):
	nom = models.CharField(max_length=100)


class Plot(models.Model):
	nom = models.CharField(max_length=100)
	description = models.TextField()


class Personne(models.Model):
	HOMME = 'm'
	FEMME = 'f'

	SEX_CHOICES = (
		(HOMME, '♂'),
		(FEMME, '♀')
	)


	nom = models.CharField(max_length=100)
	sexe = models.CharField(max_length=1, choices=SEX_CHOICES, default=HOMME)

	clan = models.ForeignKey(Clan)

	intrigue = models.SmallPositiveIntegerField()
	combat = models.SmallPositiveIntegerField()
	gestion = models.SmallPositiveIntegerField()
	diplomatie = models.SmallPositiveIntegerField()
	strategie = models.CharField(max_length=15)

	pere = models.ForeignKey('self', related_name='+', null=True, blank=True, on_delete=models.SET_NULL)
	mere = models.ForeignKey('self', related_name='+', null=True, blank=True, on_delete=models.SET_NULL)
	femme = models.ForeignKey('self', related_name='+', null=True, blank=True, on_delete=models.SET_NULL)
	fratrie = models.SmallPositiveIntegerField()

	chateau = models.ForeignKey(Chateau)
	suzerain = models.ForeignKey('self', related_name='+', null=True, blank=True, on_delete=models.SET_NULL)

	description = models.TextField()
	notes = models.TextField()
	plot = models.ForeignKey(Plot)
