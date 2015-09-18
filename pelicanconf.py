#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals


AUTHOR = u'Carlos Rodr\xedguez'
SITENAME = u'Bit\xe1cora Personaaaaaaaal'
SITEURL = ''

PATH = 'content'
#THEME = "notmyidea"
THEME = "simple"

TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = u'es'
STATIC_PATHS = ["images" ]
LOAD_CONTENT_CACHE = False
# The minimum number of articles allowed on the last page. Use this when you
# don’t want to have a last page with very few articles.
DEFAULT_ORPHANS = 0
# The maximum number of articles to include on a page, not including orphans.
DEFAULT_PAGINATION = 3
#Activate pagination.
WITH_PAGINATION = True


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
