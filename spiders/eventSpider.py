# -*- coding: utf-8 -*-
import scrapy
import re

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from EventScrapyDemo.items import EventItem



class EventspiderSpider(CrawlSpider):
    name = 'eventSpider'
    allowed_domains = ['browse.calendar.gwu.edu']
    start_urls = ['http://browse.calendar.gwu.edu/EventList.aspx?fromdate=5/20/2016&todate=8/20/2016&display=Month&view=Category']
    rules = (
        Rule(
            LinkExtractor(
                allow = (
                    'EventList.aspx?\S+$',
                    ),
                allow_domains = ("browse.calendar.gwu.edu"),
                restrict_xpaths = ("//div[@class='vevent']"),
                ),
            
            callback = 'parse_event',
            ),
    )

    def __init__(self):
        super(EventspiderSpider, self).__init__() 
        self.ID = 0


    def parse_event(self, response):
        item = EventItem()
        item = self.parse_source(response.body)
        return item


    def parse_source(self, text):
        item = EventItem()
        
        title = self.extract_title(text)
        description = self.extract_description(text)
        startDate = self.extract_startDate(text)
        endDate = self.extract_endDate(text)
        startTime = self.extract_startTime(text)
        endTime = self.extract_endTime(text)
        location = self.extract_location(text)

        self.ID += 1
        item['idEvent'] = self.ID
        item['title'] = title
        item['startDate'] = startDate
        item['startTime'] = startTime
        item['endDate'] = endDate
        item['endTime'] = endTime
        item['description'] = description
        item['remark'] = ""
        return item
    
    def extract_title(self, text):
        reobj = re.compile(r'<head id="head1"><title>[\w\W]*?</title>')
        match = reobj.search(text)
        if match:
            result = match.group()
            result = re.sub(r'<head id="head1"><title>', '', result)
            result = re.sub(r'</title>', '', result)
            result = re.sub(r'\n', '', result)
            result = re.sub(r'\t', '', result)
            result = re.sub(r'\r', '', result)
            result = re.sub(r'  ', '', result)
            result = re.sub(u'†', '', result)
            result = re.sub(r'\\x\d\d', '', result)
        else:
            result = ""
        return result

    def extract_description(self, text):
        reobj = re.compile(r'<meta id=\"description1\" name=\"description\" content=\"[\w\W]*?\" />')
        match = reobj.search(text)
        if match:
            result = match.group()
            result = unicode(result, 'utf-8')
            result = re.sub(r'<meta id=\"description1\" name=\"description\" content=\"', '', result)
            result = re.sub(r'/>', '', result)
            result = re.sub(r'\t', '', result)
            result = re.sub(r'\r', '', result)
            result = re.sub(r'\n', '', result)
            result = re.sub(u'†', '', result)
            result = re.sub(r'\\xe2\\x80\\x99', '\'', result)
        else:
            result = ""
        return result

    def extract_startDate(self, text):
        reobj = re.compile(r'Start Date:&nbsp;</b></td><td class=\"detailsview\" colspan=\"1\" width=\"25%\" nowrap=\"nowrap\">[\w\W]*?</td>')
        match = reobj.search(text)
        if match:
            result = match.group()
            result = re.sub(r'Start Date:&nbsp;</b></td><td class=\"detailsview\" colspan=\"1\" width=\"25%\" nowrap=\"nowrap\">', '', result)
            result = re.sub(r'</td>', '', result)
            result = re.sub(r'\t', '', result)
            result = re.sub(r'\r', '', result)
            result = re.sub(r'\n', '', result)
            result = re.sub(r'  ', '', result)
            result = re.sub(u'†', '', result)
            result = re.sub(r'\\x\w\w', '', result)
        else:
            result = ""
        return result

    def extract_startTime(self, text):
        reobj = re.compile(r'Start Time:&nbsp;</b></td><td class=\"detailsview\" colspan=\"1\" width=\"25%\" nowrap=\"nowrap\">[\w\W]*?</td>')
        match = reobj.search(text)
        if match:
            result = match.group()
            result = re.sub(r'Start Time:&nbsp;</b></td><td class=\"detailsview\" colspan=\"1\" width=\"25%\" nowrap=\"nowrap\">', '', result)
            result = re.sub(r'</td>', '', result)
            result = re.sub(r'\t', '', result)
            result = re.sub(r'\r', '', result)
            result = re.sub(r'\n', '', result)
            result = re.sub(r'  ', '', result)
            result = re.sub(u'†', '', result)
            result = re.sub(r'\\x\w\w', '', result)
        else:
            result = ""
        return result

    def extract_endDate(self, text):
        reobj = re.compile(r'End Date:&nbsp;</b></td><td class=\"detailsview\" colspan=\"1\" width=\"25%\" nowrap=\"nowrap\">[\w\W]*?</td>')
        match = reobj.search(text)
        if match:
            result = match.group()
            result = re.sub(r'End Date:&nbsp;</b></td><td class=\"detailsview\" colspan=\"1\" width=\"25%\" nowrap=\"nowrap\">', '', result)
            result = re.sub(r'</td>', '', result)
            result = re.sub(r'\t', '', result)
            result = re.sub(r'\r', '', result)
            result = re.sub(r'\n', '', result)
            result = re.sub(r'  ', '', result)
            result = re.sub(u'†', '', result)
            result = re.sub(r'\\x\w\w', '', result)
        else:
            result = ""
        return result

    def extract_endTime(self, text):
        reobj = re.compile(r'End Time:&nbsp;</b></td><td class=\"detailsview\" colspan=\"1\" width=\"25%\" nowrap=\"nowrap\">[\w\W]*?</td>')
        match = reobj.search(text)
        if match:
            result = match.group()
            result = re.sub(r'End Time:&nbsp;</b></td><td class=\"detailsview\" colspan=\"1\" width=\"25%\" nowrap=\"nowrap\">', '', result)
            result = re.sub(r'</td>', '', result)
            result = re.sub(r'\t', '', result)
            result = re.sub(r'\r', '', result)
            result = re.sub(r'\n', '', result)
            result = re.sub(r'  ', '', result)
            result = re.sub(u'†', '', result)
            result = re.sub(r'\\x\w\w', '', result)
        else:
            result = ""
        return result

    def extract_location(self, text):
        reobj1 = re.compile(r'<td class=\"detailsview\"><b>Location:</b>[\w\W]*?</td>')
        reobj2 = re.compile(r'<p><strong><span style=\"font-size: 13pt; font-family: Times New Roman,serif; color: #17365d;\">Location:[\w\W]*?</span></strong></p>')
        match1 = reobj1.search(text)
        if match1:
            result = match1.group()
            result = re.sub(r'<BR>', ' ', result)
            result = re.sub(r'\t', '', result)
            result = re.sub(r'\r', '', result)
            result = re.sub(r'<[\w\W]*?>', '', result)
            result = re.sub(r'\([\w\W]*?\)', '', result)
            result = re.sub(r'&nbsp;', ' ', result)
            result = re.sub(u'†', '', result)
            result = re.sub(r'\\x\w\w', '', result)
        else:
            match2 = reobj2.search(text)
            if match2:
                result = match2.group()
                result = re.sub(r'<p><strong><span [\w\W]*?>Location: ', '', result)
                result = re.sub(r'</span></strong></p>', '', result)
                result = re.sub(r'\t', '', result)
                result = re.sub(r'\r', '', result)
                result = re.sub(u'†', '', result)
                result = re.sub(r'\\x\w\w', '', result)
            else:
                result = ""
        return result