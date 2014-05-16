# -*- coding: utf-8 -*-
from django.contrib import admin

from folk.models import Chateau, Clan, Personne


class ChateauAdmin(admin.ModelAdmin):
	pass
admin.site.register(Chateau, ChateauAdmin)


class ClanAdmin(admin.ModelAdmin):
	pass
admin.site.register(Clan, ClanAdmin)


class PersonneAdmin(admin.ModelAdmin):
	list_display = ('nom', 'sexe')
	list_filter = ('clan', 'plot', 'suzerain',)
admin.site.register(Personne, PersonneAdmin)
