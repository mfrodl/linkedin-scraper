# -*- coding: utf-8 -*-

import scrapy

class LinkedinItem(scrapy.Item):
    """ Item retrieved by scraper """
    first_name = scrapy.Field()
    last_name = scrapy.Field()
    position = scrapy.Field()
    company = scrapy.Field()
    city = scrapy.Field()
    country = scrapy.Field()
