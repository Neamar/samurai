from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.dispatch import receiver
from django.db.models.signals import post_save

from game.dirty_fields import DirtyFieldsMixin


@python_2_unicode_compatible
class Perso(DirtyFieldsMixin, models.Model):
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
    description = models.TextField(blank=True, null=True)
    factions = models.ManyToManyField("Clan", related_name="+", blank=True)

    def __str__(self):
        return self.nom

    def mari(self):
        return Perso.objects.filter(femme=self)

    def enfants(self):
        return Perso.objects.filter(pere=self).order_by('naissance')

    def siblings(self):
        if not self.pere:
            return []

        return Perso.objects.filter(pere=self.pere).exclude(id=self.pk).order_by('naissance')

    def vassaux(self):
        return Perso.objects.filter(suzerain=self).order_by('-rang', '-age')


@python_2_unicode_compatible
class Clan(models.Model):
    class Meta:
        ordering = ['nom']

    nom = models.CharField(unique=True, max_length=200)
    avatar = models.ImageField(blank=True, null=True)
    leader = models.ForeignKey("Perso", related_name="+", blank=True, null=True)
    culture = models.ForeignKey("self", related_name="+", blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    richesse = models.CharField(max_length=200, blank=True, null=True)
    militaire = models.IntegerField(default=0)

    def __str__(self):
        return self.nom

    def membres(self):
        return Perso.objects.filter(clan=self).order_by('-rang', '-age')

    def expat(self):
        return Perso.objects.filter(clan_origine=self).exclude(clan=self).order_by('-rang', '-age')

    def lieux(self):
        return Lieu.objects.filter(clan=self)

    def culturistes(self):
        return Perso.objects.filter(culture=self).order_by('-rang', '-age')

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

    def sub_lieu(self):
        return Lieu.objects.filter(lieu=self)

    def residents(self):
        return Perso.objects.filter(residence=self).order_by('-rang', '-age')


class Change(models.Model):
    perso = models.ForeignKey("perso")
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)


@receiver(post_save, sender=Perso)
def handle_post_save(sender, instance, **kwargs):
    changes = Change(perso=instance)
    for key in instance.get_dirty_fields().keys():
        changes.description += "%s : %s" % (key, getattr(instance, key))
    changes.save()
