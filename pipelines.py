# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from json import *
from scrapy import signals
import json
import codecs
from scrapy.xlib.pydispatch import dispatcher

class EventscrapydemoPipeline(object):
	def process_item(self, item, spider):
		return item

class JsonWithEncodingEventPipeline(object):
	def __init__(self):
		dispatcher.connect(self.spider_opened, signals.spider_opened)
		dispatcher.connect(self.spider_closed, signals.spider_closed)


	def spider_opened(self, spider):
		self.file = codecs.open('eventGWU.json', 'w', encoding='utf-8')
		self.file.write('{"events":[\n')

	def process_item(self, item, spider):
		line = json.dumps(dict(item), ensure_ascii=False) + ",\n"
		self.file.write(line)
		return item

	def spider_closed(self, spider):
		self.file.write("]}")
		self.file.close()
