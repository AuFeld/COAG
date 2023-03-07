# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field


class JobItem(scrapy.Item):
    id = scrapy.Field()
    title = scrapy.Field()
    company = scrapy.Field()
    department = scrapy.Field()
    location = scrapy.Field()
    description = scrapy.Field()
    requirements = scrapy.Field()
    url = scrapy.Field()
    industry = scrapy.Field()
    remote_score = scrapy.Field()
    _tags = Field()
    date_posted = scrapy.Field()
    multiloc = scrapy.Field()
    slug = scrapy.Field()
    apply_url = scrapy.Field()  
    unix_timestamp = scrapy.Field()
    expired = scrapy.Field()
    flagged = scrapy.Field()


    def __repr__(self): 
        """only print out title after exiting the Pipeline"""
        return repr({"Job Title": self['title']})
