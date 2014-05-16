# -*- coding: utf-8 -*-
from django.contrib import admin

from folk.models import Chateau, Clan, Personne


class ChateauAdmin(admin.ModelAdmin):
	list_display = ('nom', 'thumb')

	def thumb(self, obj):
		return '<img src="%s" style="width:50px" />' % obj.avatar.url
	thumb.short_description = 'Thumb'
	thumb.allow_tags = True
admin.site.register(Chateau, ChateauAdmin)


class ClanAdmin(admin.ModelAdmin):
	list_display = ('nom', 'thumb')

	def thumb(self, obj):
		return '<img src="%s" style="width:50px" />' % obj.avatar.url
	thumb.short_description = 'Thumb'
	thumb.allow_tags = True

admin.site.register(Clan, ClanAdmin)


class PersonneAdmin(admin.ModelAdmin):
	list_display = ('thumb', 'nom', 'sexe', 'clan')
	list_filter = ('clan', 'plot')

	def thumb(self, obj):
		return '<img src="%s" style="width:50px" />' % obj.avatar.url
	thumb.short_description = 'Thumb'
	thumb.allow_tags = True

	def queryset(self, request):
		return super(PersonneAdmin, self).queryset(request).select_related('clan')
admin.site.register(Personne, PersonneAdmin)
