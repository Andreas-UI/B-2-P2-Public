from django import forms
from django.template.loader import get_template
from django.contrib.admin import widgets
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

from .settings import (
    PAWN_EDITOR_RESIZEABLE, 
    PAWN_URLS_PATH, 
    PAWN_SERVER_CALL_LATENCY, 
    PAWN_UPLOAD_URLS_PATH
)

try:
    DEBUG = getattr(settings, 'DEBUG', False)
except ImproperlyConfigured:
    # Documentations work around.
    DEBUG = False

minified = '.min' if not DEBUG else str()

class PawnWidget(forms.Textarea):
    template_name = 'pawn/widget.html'

    def get_context(self, name, value, attrs=None):
        try:
            attrs.update(self.add_pawn_attrs(attrs))
        except AttributeError:
            attrs = self.add_pawn_attrs(attrs)

        return super(PawnWidget, self).get_context(name, value, attrs)

    def render(self, name, value, attrs=None, renderer=None):
        attrs.update(self.attrs)
        attrs.update(self.add_pawn_attrs(attrs))

        return super(PawnWidget, self).render(name, value, attrs, renderer)

    @staticmethod
    def add_pawn_attrs(attrs):
        if 'class' in attrs.keys():
            attrs['class'] += ' pawn-editor'
        else:
            attrs.update({
                'class': 'pawn-editor'
            })

        attrs.update({
            'data-pawn-editor-resizable': PAWN_EDITOR_RESIZEABLE,
            'data-pawn-urls-path': PAWN_URLS_PATH,
            'data-pawn-upload-urls-path': PAWN_UPLOAD_URLS_PATH,
            'data-pawn-latency': PAWN_SERVER_CALL_LATENCY, 
            'rows': "1",
        })

        return attrs

    class Media:
        js = [
            # 'pawn/js/pawn{}.js'.format(minified),
            'pawn/js/pawn.js',
        ]

        css = {
            'all' : ['pawn/css/style.css']
        }


class AdminPawnWidget(PawnWidget, widgets.AdminTextareaWidget):
    class Media:
        css = {
            # 'all': ['pawn/admin/css/pawn{}.css'.format(minified)]
            'all': ['pawn/admin/css/pawn.css']
        }

        js = [
            # 'pawn/js/pawn{}.js'.format(minified),
            'pawn/js/pawn.js',
        ]