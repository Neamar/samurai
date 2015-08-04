from django.db import models


class Perso(models.Model):
    nom = models.CharField(max_length=200)
    avatar = models.ImageField(blank=True, null=True)
    sexe = models.CharField(max_length=200)
    age = models.CharField(max_length=200)
    pere = models.ForeignKey("self")
    femme = models.ForeignKey("self", related_name="+")
    suzerain = models.ForeignKey("self", related_name="+")
    clan = models.ForeignKey("Clan")
    clan_origine = models.ForeignKey("Clan", related_name="+")
    culture = models.ForeignKey("Culture")
    religion = models.ForeignKey("Religion")
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

    def __unicode__(self):
        return self.nom


class Clan(models.Model):
    nom = models.CharField(max_length=200)
    avatar = models.ImageField(blank=True, null=True)
    leader = models.ForeignKey("Perso", related_name="+")
    culture = models.CharField(max_length=200)
    description = models.TextField()
    tresorerie = models.IntegerField()

    def __unicode__(self):
        return self.nom


class Unite(models.Model):
    nom = models.CharField(max_length=200)
    position = models.ForeignKey("Lieu")
    commandant = models.ForeignKey("Perso")
    nombre = models.IntegerField()
    entrainement = models.IntegerField()
    description = models.TextField()
    experience = models.CharField(max_length=200)
    moral = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nom


class Lieu(models.Model):
    nom = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    image = models.ImageField(blank=True, null=True)

    chef = models.ForeignKey("perso")
    population = models.IntegerField()
    description = models.TextField()

    def __unicode__(self):
        return self.nom


class Culture(models.Model):
    nom = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nom


class Religion(models.Model):
    nom = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nom
