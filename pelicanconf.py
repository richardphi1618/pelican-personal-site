AUTHOR = 'Richard Blanchette'
SITEURL = 'https://www.richardphi.dev'

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'


SITENAME = "Richard Blanchette Personal Site"
SITETITLE = "Richardphi.dev"
SITESUBTITLE = "Professional Problem Solver"
SITEDESCRIPTION = "Richard Blanchette's Thoughts and Writings"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

MENUITEMS = (
    ("Archives", "/archives.html"),
    ("Categories", "/categories.html"),
    ("Tags", "/tags.html"),
)

# Social widget
SOCIAL = (
    ("linkedin", "https://www.linkedin.com/in/richphi/"),
    ("github", "https://github.com/richardphi1618"),
    ("twitter", "https://twitter.com/rich_phi"),
)

DEFAULT_PAGINATION = 10

THEME = "./pelican-themes/Flex"
THEME_COLOR = 'dark'
THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
THEME_COLOR_ENABLE_USER_OVERRIDE = True

PYGMENTS_STYLE = 'emacs'
PYGMENTS_STYLE_DARK = 'monokai'

BROWSER_COLOR = "#38761d"
ROBOTS = "index, follow"

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

PORT=5051
