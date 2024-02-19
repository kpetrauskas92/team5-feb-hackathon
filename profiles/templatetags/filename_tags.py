from django import template
register = template.Library()


@register.filter
def filename(value):
    """Extracts the filename from a file path."""
    import os
    return os.path.basename(value)
