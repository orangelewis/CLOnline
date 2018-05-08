# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoItem
from article.models import Film_article

class FilmspiderItem(DjangoItem):
    # define the fields for your item here like:
    # name = scrapy.Field()
    django_model = Film_article
    pass
