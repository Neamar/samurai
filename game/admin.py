from django.contrib import admin

from game.models import Perso, Clan, Lieu


@admin.register(Perso)
class PersoAdmin(admin.ModelAdmin):
    change_form_template = 'change_form_perso.html'
    # fieldsets = (
    #     (None, {
    #         "fields": [f for f in Perso._meta.get_all_field_names() if f != "notes_mj"]
    #     }),
    #     ('Notes MJ', {
    #         'classes': ('collapse',),
    #         'fields': ('notes_mj',)
    #     }),
    # )
    list_filter = (
        'sexe',
        ('clan', admin.RelatedOnlyFieldListFilter),
        ('clan_origine', admin.RelatedOnlyFieldListFilter),
        ('culture', admin.RelatedOnlyFieldListFilter),
        ('residence', admin.RelatedOnlyFieldListFilter)
    )
    list_max_show_all = 5000
    save_on_top = True
    search_fields = ('nom', 'clan__nom')
    ordering = ("nom",)
    list_display = ('nom', 'sexe', 'clan', 'img')

    def img(self, perso):
        if perso.avatar:
            return u"<img src=\"/media/%s\" />" % perso.avatar
        else:
            return False
    img.description = "Avatar"
    img.allow_tags = True


@admin.register(Clan)
class ClanAdmin(admin.ModelAdmin):
    change_form_template = 'change_form_clan.html'
    list_display = ('nom', 'img')

    def img(self, clan):
        if clan.avatar:
            return u"<img src=\"/media/%s\" />" % clan.avatar
        else:
            return False
    img.description = "Avatar"
    img.allow_tags = True

    ordering = ("nom",)


@admin.register(Lieu)
class LieuAdmin(admin.ModelAdmin):
    change_form_template = 'change_form_lieu.html'

    search_fields = ('nom',)
    list_display = ('nom', 'img')

    def img(self, lieu):
        if lieu.image:
            return u"<img src=\"/media/%s\" />" % lieu.image
        else:
            return False
    img.description = "Avatar"
    img.allow_tags = True

    ordering = ("nom",)
