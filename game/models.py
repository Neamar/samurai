from django.db import models


class Perso(models.Model):
    HOMME = "homme"
    FEMME = "femme"
    SEXE_CHOICES = (
        (HOMME, "Homme"),
        (FEMME, "Femme"),
    )

    nom = models.CharField(max_length=200)
    avatar = models.ImageField(blank=True, null=True)
    sexe = models.CharField(max_length=200, choices=SEXE_CHOICES)
    age = models.CharField(max_length=200, blank=True, null=True)
    pere = models.ForeignKey(
        "self",
        blank=True,
        null=True,
        limit_choices_to={"sexe": HOMME}
    )
    femme = models.ForeignKey(
        "self",
        related_name="+",
        blank=True,
        null=True,
        limit_choices_to={'sexe': FEMME}
    )

    suzerain = models.ForeignKey("self", related_name="+", blank=True, null=True)
    clan = models.ForeignKey("Clan", blank=True, null=True)
    clan_origine = models.ForeignKey("Clan", related_name="+", blank=True, null=True)
    factions = models.ManyToManyField("Clan", related_name="+", blank=True)
    culture = models.ForeignKey("Culture", blank=True, null=True)
    position = models.TextField(blank=True, null=True)
    residence = models.ForeignKey("Lieu")
    occupation = models.TextField(blank=True, null=True)
    naissance = models.CharField(max_length=200, blank=True, null=True)
    rang = models.CharField(max_length=200, blank=True, null=True)
    loyaute = models.CharField(max_length=200, blank=True, null=True)
    foi = models.CharField(max_length=200, blank=True, null=True)
    compassion = models.CharField(max_length=200, blank=True, null=True)
    honneur = models.CharField(max_length=200, blank=True, null=True)
    influence = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    education = models.CharField(max_length=200, blank=True, null=True)
    charme = models.CharField(max_length=200, blank=True, null=True)
    patience = models.CharField(max_length=200, blank=True, null=True)
    finesse = models.CharField(max_length=200, blank=True, null=True)
    assurance = models.CharField(max_length=200, blank=True, null=True)
    notes_mj = models.TextField(blank=True, null=True)
    secret_1 = models.TextField(blank=True, null=True)
    secret_2 = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.nom


class Clan(models.Model):
    nom = models.CharField(max_length=200)
    avatar = models.ImageField(blank=True, null=True)
    leader = models.ForeignKey("Perso", related_name="+", blank=True, null=True)
    culture = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    tresorerie = models.IntegerField(default=0)

    def __unicode__(self):
        return self.nom


class Lieu(models.Model):
    class Meta:
        verbose_name_plural = "lieux"

    nom = models.CharField(max_length=200, blank=True, null=True)
    type = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(blank=True, null=True)

    chef = models.ForeignKey("perso", blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    lieu = models.ForeignKey("self", related_name="+", blank=True, null=True)
    clan = models.ForeignKey("Clan", blank=True, null=True)

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
