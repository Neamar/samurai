from django.db import models


class Perso(models.Model):
    nom = models.CharField(max_length=200)
    sexe = models.CharField(max_length=200)
    age = models.CharField(max_length=200)
    pere = models.ForeignKey("self")
    femme = models.ForeignKey("self", related_name="+")
    suzerain = models.ForeignKey("self", related_name="+")
    clan = models.ForeignKey("Clan")
    clan_origine = models.ForeignKey("Clan", related_name="+")
    culture = models.CharField(max_length=200)
    religion = models.CharField(max_length=200)
    position = models.TextField()
    residence = models.ForeignKey("Lieu")
    occupation = models.TextField()
    naissance = models.CharField(max_length=200)
    rang = models.CharField(max_length=200)
    loyaute = models.CharField(max_length=200)
    foi = models.CharField(max_length=200)
    compassion = models.CharField(max_length=200)
    honneur = models.CharField(max_length=200)
    influence = models.CharField(max_length=200)
    description = models.TextField()
    education = models.CharField(max_length=200)
    chargme = models.CharField(max_length=200)
    patience = models.CharField(max_length=200)
    finesse = models.CharField(max_length=200)
    assurance = models.CharField(max_length=200)
    suite = models.TextField()
    notes_mj = models.TextField()


class Clan(models.Model):
    nom = models.CharField(max_length=200)
    leader = models.ForeignKey("Perso", related_name="+")
    culture = models.CharField(max_length=200)
    description = models.TextField()
    tresorerie = models.IntegerField()


class Unite(models.Model):
    nom = models.CharField(max_length=200)
    position = models.ForeignKey("Lieu")
    commandant = models.ForeignKey("Perso")
    nombre = models.IntegerField()
    entrainement = models.IntegerField()
    description = models.TextField()
    experience = models.CharField(max_length=200)
    moral = models.CharField(max_length=200)


class Lieu(models.Model):
    nom = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    chef = models.ForeignKey("perso")
    population = models.IntegerField()
    description = models.TextField()
