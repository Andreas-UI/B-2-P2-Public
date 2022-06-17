from django.conf import settings

# https://facelessuser.github.io/pymdown-extensions/
# https://www.markdownguide.org/

LATENCY = 500
# Markdownify
PAWN_MARKDOWNIFY_FUNCTION = getattr(settings, 'PAWN_MARKDOWNIFY_FUNCTION', 'pawn.utils.markdownify')
PAWN_SERVER_CALL_LATENCY = getattr(settings, 'PAWN_SERVER_CALL_LATENCY', LATENCY)

from .caption import captionExtension

# Extensions
PAWN_EXTENSIONS = [
    'tables', 
    'fenced_code', 
    'footnotes', 
    'def_list', 
    'abbr', 
    'attr_list', 
    'sane_lists', 
    'smarty',
    'pymdownx.tilde', 
    'pymdownx.tasklist', 
    captionExtension(stripTitle=False)]


PAWN_MARKDOWN_EXTENSIONS = getattr(settings, 'PAWN_MARKDOWN_EXTENSIONS', PAWN_EXTENSIONS)
PAWN_MARKDOWN_EXTENSION_CONFIGS = getattr(settings, 'PAWN_MARKDOWN_EXTENSION_CONFIGS', dict())

# Editor
PAWN_EDITOR_RESIZEABLE = getattr(settings, 'PAWN_EDITOR_RESIZEABLE', True)

# Urls
PAWN_URLS_PATH = getattr(settings, 'PAWN_URLS_PATH', '/pawn/markdownify/')
PAWN_UPLOAD_URLS_PATH = getattr(settings, 'PAWN_UPLOAD_URLS_PATH', "/pawn/upload/")

# Media
from datetime import datetime
PAWN_MEDIA_PATH = datetime.now().strftime('pawn/%Y/%m/%d')

FIFTY_MEGABYTES = 50 * 1024 * 1024
VALID_CONTENT_TYPES = 'image/jpeg', 'image/png', 'image/svg+xml', 'image/gif', 'image/webp'
NINETY_DPI = 90

# 1920 x 1080
IM_WIDTH = 1920
IM_HEIGHT = 1080

PAWN_UPLOAD_MAX_SIZE = getattr(settings, 'PAWN_UPLOAD_MAX_SIZE', FIFTY_MEGABYTES)

PAWN_UPLOAD_CONTENT_TYPES = getattr(settings, 'PAWN_UPLOAD_CONTENT_TYPES', VALID_CONTENT_TYPES)

PAWN_IMAGE_MAX_SIZE = getattr(settings, 'PAWN_IMAGE_MAX_SIZE', dict(size=(IM_WIDTH, IM_HEIGHT), quality=NINETY_DPI))

PAWN_SVG_JAVASCRIPT_PROTECTION = True