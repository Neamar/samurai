from django.contrib import admin

from game.models import Perso, Clan, Lieu, Culture, Religion

admin.site.register(Perso)
admin.site.register(Clan)
admin.site.register(Lieu)
admin.site.register(Culture)
admin.site.register(Religion)
