# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
from scrapy.conf import settings
from scrapy.exceptions import DropItem
from scrapy import log

class DuplicatesPipeline(object):
	def __init__(self):
		self.ids_seen = set()
		
	def process_item(self, item, spider):
		if item['link'] in self.ids_seen:
			raise DropItem("Duplicate item found: %s" % item)
		else:
			self.ids_seen.add(item['link'])
		return item
		
class MongoDBPipeline(object):
	def __init__(self):
		connection = pymongo.MongoClient(
			settings['MONGODB_SERVER'],
			settings['MONGODB_PORT']
		)
		db = connection[settings['MONGODB_DB']]
		self.collection = db[settings['MONGODB_COLLECTION']]
		
	def process_item(self, item, spider):
		valid = True
		for data in item:
			if not data:
				valid = False
				raise DropItem("Missing{0}!".format(data))
			if valid:
				self.collection.insert(dict(item))
				log.msg("Added to MongoDB database!", 
				level=log.DEBUG, spider = spider)
			return item