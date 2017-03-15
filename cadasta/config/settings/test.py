from .dev import *  # NOQA

MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'core/media/test')
JSONATTRS_SCHEMA_SELECTORS['core.mysanitizefieldsmodel'] = ()
