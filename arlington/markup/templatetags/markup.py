"""
Set of "markup" template filters for Django.  These filters transform plain text
markup syntaxes to HTML; currently there is support for:

    * Textile, which requires the PyTextile library available at
      http://loopcore.com/python-textile/

    * Markdown, which requires the Python-markdown library from
      http://www.freewisdom.org/projects/python-markdown

    * reStructuredText, which requires docutils from http://docutils.sf.net/
"""

from django import template
from django.conf import settings
from django.utils.encoding import force_bytes, force_text
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(is_safe=True)
def textile(value):
    try:
        import textile
    except ImportError:
        if settings.DEBUG:
            raise template.TemplateSyntaxError("Error in 'textile' filter: The Python textile library isn't installed.")
        return force_text(value)
    else:
        return mark_safe(force_text(textile.textile(force_bytes(value), encoding='utf-8', output='utf-8')))

@register.filter(is_safe=True)
def markdown(value, arg=''):
    """
    Runs Markdown over a given value, optionally using various
    extensions python-markdown supports.

    Syntax::

        {{ value|markdown:"extension1_name,extension2_name..." }}

    To enable safe mode, which strips raw HTML and only returns HTML
    generated by actual Markdown syntax, pass "safe" as the first
    extension in the list.

    If the version of Markdown in use does not support extensions,
    they will be silently ignored.

    """
    try:
        import markdown
    except ImportError:
        if settings.DEBUG:
            raise template.TemplateSyntaxError("Error in 'markdown' filter: The Python markdown library isn't installed.")
        return force_text(value)
    else:
        markdown_vers = getattr(markdown, "version_info", 0)
        if markdown_vers < (2, 1):
            if settings.DEBUG:
                raise template.TemplateSyntaxError(
                    "Error in 'markdown' filter: Django does not support versions of the Python markdown library < 2.1.")
            return force_text(value)
        else:
            extensions = [e for e in arg.split(",") if e]
            if extensions and extensions[0] == "safe":
                extensions = extensions[1:]
                return mark_safe(markdown.markdown(
                    force_text(value), extensions, safe_mode=True, enable_attributes=False))
            else:
                return mark_safe(markdown.markdown(
                    force_text(value), extensions, safe_mode=False))

@register.filter(is_safe=True)
def restructuredtext(value):
    import warnings
    warnings.warn('The restructuredtext filter has been deprecated',
                  category=DeprecationWarning)
    try:
        from docutils.core import publish_parts
    except ImportError:
        if settings.DEBUG:
            raise template.TemplateSyntaxError("Error in 'restructuredtext' filter: The Python docutils library isn't installed.")
        return force_text(value)
    else:
        docutils_settings = getattr(settings, "RESTRUCTUREDTEXT_FILTER_SETTINGS", {})
        parts = publish_parts(source=force_bytes(value), writer_name="html4css1", settings_overrides=docutils_settings)
        return mark_safe(force_text(parts["fragment"]))
