from django.contrib import admin

from game.models import Perso, Clan, Lieu, Change
from django.template.loader import get_template


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

    list_display = ('nom', 'sexe', 'details', 'rang', 'clan', 'img', "residence")

    def img(self, perso):
        if perso.avatar:
            return u"<img src=\"/media/%s\" width=60 height=60 />" % perso.avatar
        else:
            return False
    img.description = "Avatar"
    img.allow_tags = True

    def details(self, perso):
        det = (
            ("D:", perso.description),
            ("O:", perso.occupation),
            ("P:", perso.position),

        )
        return "<br>".join("<b>%s</b> : %s" % (k, v) for k, v in det if v != "")
    details.allow_tags = True


    inlines = [ChangesInline]

@admin.register(Clan)
class ClanAdmin(admin.ModelAdmin):
    search_fields = ('nom,',)

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

    fieldsets = (
        (None, {
            "fields": ('nom', 'type', 'image', 'chef', 'lieu', 'clan')
        }),
        ('Autres', {
            'classes': ('collapse',),
            'fields': ('image_large', 'description')
        }),
    )

    change_form_template = 'change_form_lieu.html'

    search_fields = ('nom',)
    list_display = ('nom', 'img', 'clan', 'lieu')

    def img(self, lieu):
        if lieu.image:
            return u"<img src=\"/media/%s\" width='60' height='60'/>" % lieu.image
        else:
            return False
    img.description = "Avatar"
    img.allow_tags = True

    ordering = ("nom",)


template = get_template('id_perso.html')


@admin.register(Change)
class ChangeAdmin(admin.ModelAdmin):
    search_fields = ('perso__nom, description',)
    list_display = ('pk', 'personnage', 'clan', 'desc')

    def personnage(self, change):
        return template.render({"perso": change.perso})

        # return u"<a href=\"/admin/game/perso/%s\">%s</a>" % (change.perso.pk, change.perso)
    personnage.allow_tags = True

    def clan(self, change):
        return "<img title='%s' src='/media/%s' width=40 height=40 />" % (change.perso.clan, change.perso.clan.avatar if change.perso.clan else "")

    clan.allow_tags = True

    def desc(self, change):
        try:
            return "<br>".join(["<b>%s</b>: %s" % (key, value) for key, value in [atomic.split(":") for atomic in change.description.strip().split("\n")]])
        except:
            return change.description.replace("\n", "<br>")
    desc.allow_tags = True

    ordering = ("-date",)
