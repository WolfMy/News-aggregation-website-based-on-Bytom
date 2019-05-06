# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field

class RedditItem(Item):
	subreddit = Field()
	link = Field()
	title = Field()
	date = Field()
	bote = Field()
	top_comment = Field()
