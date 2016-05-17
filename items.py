# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class EventItem(scrapy.Item):
	idEvent = scrapy.Field()
	title = scrapy.Field()
	location = scrapy.Field()
	startTime = scrapy.Field()
	endTime = scrapy.Field()
	startDate = scrapy.Field()
	endDate = scrapy.Field()
	description = scrapy.Field()
	remark = scrapy.Field()

