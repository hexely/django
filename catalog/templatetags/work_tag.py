from django import template
from django.conf import settings

register = template.Library()


@register.filter()
def media(image):
    return f"{settings.MEDIA_URL}/{image}"


@register.simple_tag()
def media_tag(image):
    return f"{settings.MEDIA_URL}/{image}"
