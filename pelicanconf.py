# -*- coding: utf-8 -*-


AUTHOR = 'Jonathan Chancey'
SITENAME = "temtem.tech"
SITESUBTITLE = 'Your One Stop Shop for Temtem Content'
SITEURL = 'http://temtem.tech'
TIMEZONE = "US/Pacific"

# can be useful in development, but set to False when you're ready to publish
RELATIVE_URLS = True

PLUGIN_PATHS = ['plugins']
PLUGINS = [
    'assets',
    'pelican_advance_embed_tweet',
    'neighbors',
]

GITHUB_URL = 'https://github.com/chancey-dev/'
DISQUS_SITENAME = "temtem-tech"
COMMENTS_ON_PAGES = True
REVERSE_CATEGORY_ORDER = True
LOCALE = "C"
DEFAULT_PAGINATION = 4
DEFAULT_DATE = (2012, 3, 2, 14, 1, 1)

FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/{slug}.rss.xml'

# LINKS = (('Biologeek', 'http://biologeek.org'),
#          ('Filyb', "http://filyb.info/"),
#          ('Libert-fr', "http://www.libert-fr.com"),
#          ('N1k0', "http://prendreuncafe.com/blog/"),
#          ('Tarek Ziadé', "http://ziade.org/blog"),
#          ('Zubin Mithra', "http://zubin71.wordpress.com/"),)

SOCIAL = (('twitter', 'http://twitter.com/chancey_dev'),
          ('github', 'http://github.com/jonathanchancey'),)

# global metadata to all the contents
DEFAULT_METADATA = {'yeah': 'it is'}

# path-specific metadata
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    }

# static paths will be copied without parsing their contents
STATIC_PATHS = [
    'pictures',
    'extra/robots.txt',
    ]

# # custom page generated with a jinja2 template
# TEMPLATE_PAGES = {'pages/jinja2_template.html': 'jinja2_template.html'}

# code blocks with line numbers
PYGMENTS_RST_OPTIONS = {'linenos': 'table'}

# foobar will not be used, because it's not in caps. All configuration keys
# have to be in caps
foobar = "barbaz"

THEME = 'themes/eevee'
OUTPUT_PATH = 'output'
PATH = 'content'

ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{slug}/index.html'

# Custom Home page
DIRECT_TEMPLATES = (('index', 'tags', 'categories', 'archives'))
PAGINATED_TEMPLATES = (('base',))
# TEMPLATE_PAGES = {'home.html': 'index.html',}



# Eevee config
# MENUITEMS = (('Contact', '/contact/'), ('Software', '/software/'),
#              ('Donate', '/donate/'))
DISPLAY_PAGES_ON_MENU = True

DISCLAIMER = 'All trademarks are the property of their respective owners. Powered by love &amp; marshmallow fluffs.'


# THEME_PRIMARY = 'light_blue'
# THEME_ACCENT = 'deep_purple'

THEME_PRIMARY = 'blue_grey'
THEME_ACCENT = 'deep_purple'

USE_AUTHOR_CARD = False
AUTHOR_CARD_DESCRIPTION = 'My name is Kura and I break things.'

AUTHOR_CARD_SOCIAL = (('<i class="fa fa-github aria-hidden="true"></i>',
                       'https://github.com/kura'),
                      ('<i class="fa fa-twitter aria-hidden="true"></i>',
                       'https://twitter.com/kuramanga'), )

ARCHIVES_URL = 'archives.html'
ARCHIVES_SAVE_AS = 'archives.html'


