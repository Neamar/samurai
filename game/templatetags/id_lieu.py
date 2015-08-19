from django import template

register = template.Library()


@register.inclusion_tag('id_lieu.html')
def id_lieu(lieu):
    return {
        "lieu": lieu
    }
