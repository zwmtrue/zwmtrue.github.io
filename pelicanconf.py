#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Weiming "William" Zhu'
SITENAME = "Weiming's Blog"
SITEURL = 'https://zwmtrue.github.io'

PATH = 'content'
THEME = 'C:\\Users\\zwmtrue\\Documents\\pelican-themes\\pelican-themes\\bootstrap2'
TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (
         #('You can modify those links in your config file', '#'),
#		 )

#Social widget
SOCIAL = (('LinkedIn', 'https://www.linkedin.com/in/weiming-zhu-36039b5a/'),  
#         ('Another social link', '#'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
MARKUP = ('md', 'ipynb')

PLUGIN_PATH = './plugins'
PLUGINS = ['ipynb.markup']