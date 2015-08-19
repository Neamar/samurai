from django import template

register = template.Library()


@register.inclusion_tag('id_perso.html')
def id_perso(perso):
    return {
        perso: perso
    }
