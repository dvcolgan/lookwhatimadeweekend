from django import template
from django.conf import settings
from django.utils.safestring import mark_safe
from django.template.defaultfilters import stringfilter
from django.utils.encoding import force_unicode
from django.utils.safestring import mark_safe
import markdown2

register = template.Library()

@register.simple_tag
def setting(name):
    return getattr(settings, name, "")

@register.filter(is_safe=True)
@stringfilter
def markdown(value):
    return mark_safe(markdown2.markdown(force_unicode(value),safe_mode=True))
