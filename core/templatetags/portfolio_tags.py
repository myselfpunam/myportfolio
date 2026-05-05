from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def split_paragraphs(value):
    """Split text into paragraphs on double newlines."""
    if not value:
        return []
    paragraphs = [p.strip() for p in value.split('\n\n') if p.strip()]
    if not paragraphs:
        paragraphs = [value.strip()]
    return paragraphs


@register.filter
def split_newlines(value):
    """Split HTML (after linebreaksbr) on <br> tags into paragraphs."""
    if not value:
        return []
    import re
    # Split on double line breaks
    parts = re.split(r'\n\n+', str(value))
    return [p.strip() for p in parts if p.strip()]


@register.filter
def mod_clamp(value):
    """Return (value % 4) + 1 clamped to 1–4 for reveal delay classes."""
    try:
        return ((int(value) - 1) % 4) + 1
    except (ValueError, TypeError):
        return 1


@register.filter(name='add_str')
def add_str(value, arg):
    return str(value) + str(arg)
