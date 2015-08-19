from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Perso(models.Model):
    class Meta:
        ordering = ['nom']

    HOMME = "H"
    FEMME = "F"
    SEXE_CHOICES = (
        (HOMME, "Homme"),
        (FEMME, "Femme"),
    )

    nom = models.CharField(unique=True, max_length=200)
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

    rang = models.CharField(max_length=200, blank=True, null=True)
    suzerain = models.ForeignKey("self", related_name="+", blank=True, null=True)
    clan = models.ForeignKey("Clan", blank=True, null=True)
    clan_origine = models.ForeignKey("Clan", related_name="+", blank=True, null=True)
    culture = models.ForeignKey("Clan", related_name="+", blank=True, null=True)
    position = models.TextField(blank=True, null=True)
    residence = models.ForeignKey("Lieu", blank=True, null=True)
    occupation = models.TextField(blank=True, null=True)
    naissance = models.CharField(max_length=200, blank=True, null=True)
    secret_1 = models.TextField(blank=True, null=True)
    secret_2 = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    factions = models.ManyToManyField("Clan", related_name="+", blank=True)

    def __str__(self):
        return self.nom


@python_2_unicode_compatible
class Clan(models.Model):
    class Meta:
        ordering = ['nom']

    nom = models.CharField(unique=True, max_length=200)
    avatar = models.ImageField(blank=True, null=True)
    leader = models.ForeignKey("Perso", related_name="+", blank=True, null=True)
    culture = models.ForeignKey("self", related_name="+", blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    tresorerie = models.IntegerField(default=0)

    def __str__(self):
        return self.nom


@python_2_unicode_compatible
class Lieu(models.Model):
    class Meta:
        verbose_name_plural = "lieux"
        ordering = ['nom']

    nom = models.CharField(unique=True, max_length=200, blank=True, null=True)
    type = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    image_large = models.ImageField(blank=True, null=True)

    chef = models.ForeignKey("perso", blank=True, null=True)
    lieu = models.ForeignKey("self", related_name="+", blank=True, null=True)
    clan = models.ForeignKey("Clan", blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nom
