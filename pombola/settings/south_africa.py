import re

from .base import *
from .south_africa_base import *

HAYSTACK_CONNECTIONS['default']['EXCLUDED_INDEXES'] = [
    'pombola.search.search_indexes.PlaceIndex',
    'speeches.search_indexes.SpeechIndex',
]

INSTALLED_APPS = insert_after(INSTALLED_APPS,
                              'markitup',
                              'pombola.' + COUNTRY_APP)

INSTALLED_APPS += OPTIONAL_APPS

# This is needed by the speeches application
MIDDLEWARE_CLASSES += ( 'pombola.middleware.FakeInstanceMiddleware', )

ENABLED_FEATURES = make_enabled_features(INSTALLED_APPS, ALL_OPTIONAL_APPS)

PIPELINE_CSS.update(COUNTRY_CSS)
PIPELINE_JS.update(COUNTRY_JS)

EXCLUDE_FROM_SEARCH = ('places', 'info_pages');
