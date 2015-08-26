from django.contrib import admin

from game.models import Perso, Clan, Lieu, Change


class ChangesInline(admin.TabularInline):
    model = Change
    # exclude = ('secrets',)
    extra = 0


@admin.register(Perso)
class PersoAdmin(admin.ModelAdmin):
    change_form_template = 'change_form_perso.html'
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
    list_display = ('nom', 'sexe', 'description', 'rang', 'clan', 'img')

    def img(self, perso):
        if perso.avatar:
            return u"<img src=\"/media/%s\" />" % perso.avatar
        else:
            return False
    img.description = "Avatar"
    img.allow_tags = True

    inlines = [ChangesInline]

@admin.register(Clan)
class ClanAdmin(admin.ModelAdmin):
    list_filter = (
        ('culture', admin.RelatedOnlyFieldListFilter),
    )

    change_form_template = 'change_form_clan.html'
    list_display = ('nom', 'img', "richesse", "militaire")

    def img(self, clan):
        if clan.avatar:
            return u"<img src=\"/media/%s\" width='48' height='48'/>" % clan.avatar
        else:
            return False
    img.description = "Avatar"
    img.allow_tags = True

    ordering = ("nom",)


@admin.register(Lieu)
class LieuAdmin(admin.ModelAdmin):
    list_filter = (
        ('lieu', admin.RelatedOnlyFieldListFilter),
        ('clan', admin.RelatedOnlyFieldListFilter),
    )

    change_form_template = 'change_form_lieu.html'

    search_fields = ('nom',)
    list_display = ('nom', 'img', 'clan', 'lieu')

    def img(self, lieu):
        if lieu.image:
            return u"<img src=\"/media/%s\" />" % lieu.image
        else:
            return False
    img.description = "Avatar"
    img.allow_tags = True

    ordering = ("nom",)



@admin.register(Change)
class ChangeAdmin(admin.ModelAdmin):
    search_fields = ('perso__nom, description',)
    list_display = ('perso', 'description')

    ordering = ("-date",)
