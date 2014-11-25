COUNTRY_APP = 'kenya'

OPTIONAL_APPS = [
    'pombola.hansard',
    'pombola.projects',
    'pombola.place_data',
    'pombola.votematch',
]

TWITTER_USERNAME = 'MzalendoWatch'
TWITTER_WIDGET_ID = '354553209517404160'

BLOG_RSS_FEED = 'http://www.mzalendo.com/feed/'

MAP_BOUNDING_BOX_NORTH = 5.06
MAP_BOUNDING_BOX_EAST = 41.91
MAP_BOUNDING_BOX_SOUTH = -4.73
MAP_BOUNDING_BOX_WEST = 33.83

MAPIT_COUNTRY = 'KE'

COUNTRY_CSS = {
    'kenya': {
        'source_filenames': (
            # .scss files for Kenya
            'sass/kenya.scss',
            # .css files for Kenya
            'css/jquery.countdown-v1.6.0.css',
            'css/jquery-ui-1.8.17.custom.css',
            'css/admin.css',
        ),
        'output_filename': 'css/kenya.css'
    },
    'election-2013': {
        'source_filenames': (
            'kenya/election-homepage/base.css',
            'kenya/election-homepage/style.css',
        ),
        'output_filename': 'css/election-2013.css'
    },
    'intro': {
        'source_filenames': (
            'kenya/intro/intro.css',
        ),
        'output_filename': 'css/kenya-intro.css'
    },
    'shujaaz': {
        'source_filenames': (
            'shujaaz/css/bootstrap.css',
            'shujaaz/css/bootstrap-responsive.css',
            'shujaaz/css/flat-ui.css',
            'shujaaz/css/icon-font.css',

            'shujaaz/css/style.css',
        ),
        'output_filename': 'css/shujaaz.css',
    },
}

COUNTRY_JS = {
    'click-tracking': {
        'source_filenames': (
            'js/click-tracking.js',
        ),
        'output_filename': 'js/kenya.js',
        'template_name': 'pipeline/js-array.html',
    },
    'shujaaz-lt-ie8': {
        'source_filenames': (
            'shujaaz/js/icon-font-ie7.js',
        ),
        'output_filename': 'js/shujaaz-lt-ie8.js',
    },
    'shujaaz': {
        'source_filenames': (
            'shujaaz/js/jquery-1.8.3.min.js',
            'shujaaz/js/bootstrap.min.js',
            'shujaaz/js/jquery.scrollTo-1.4.3.1-min.js',
            'shujaaz/js/jquery.parallax.min.js',
            'shujaaz/js/startup-kit.js',
            'shujaaz/js/script.js',
        ),
        'output_filename': 'js/shujaaz.js',
    }
}
