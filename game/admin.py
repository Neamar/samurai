from django.contrib import admin

from game.models import Perso, Clan, Lieu


@admin.register(Perso)
class PersoAdmin(admin.ModelAdmin):
    # fieldsets = (
    #     (None, {
    #         "fields": [f for f in Perso._meta.get_all_field_names() if f != "notes_mj"]
    #     }),
    #     ('Notes MJ', {
    #         'classes': ('collapse',),
    #         'fields': ('notes_mj',)
    #     }),
    # )
    list_filter = ('sexe', 'clan', 'factions', 'culture', 'residence')
    list_max_show_all = 5000
    save_on_top = True
    search_fields = ('nom', 'clan__nom')
    ordering = ("nom",)

admin.site.register(Clan)
admin.site.register(Lieu)
