# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GeekbuyingscraperItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    price = scrapy.Field()
    review = scrapy.Field()
    like = scrapy.Field()
    image = scrapy.Field()
    link = scrapy.Field()
    item_id = scrapy.Field()
    category = scrapy.Field()
