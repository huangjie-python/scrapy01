# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import re
from zbbnews import Tool


class ZbbxwSpider(CrawlSpider):
    name = 'zbbxw'
    allowed_domains = ['www.chinaipo.com']
    start_urls = ['http://www.chinaipo.com/news/128324.html']

    rules = (
        Rule(LinkExtractor(allow=r'http:\/\/www\.chinaipo\.com\/[a-z]*?\/'),  follow=True),
        Rule(LinkExtractor(allow=r'http:\/\/www\.chinaipo\.com\/[a-z]*?\/list\d+\.html'),  follow=True),
        Rule(LinkExtractor(allow=r'.*?\d+\.html'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        item = {}
        item['title'] = re.findall(r'<h1 class="c-article__title">(.*?)<\/h1>', response.text)[0]
        item['author'] = re.findall(r'<div class="c-article__author">(.*?) · \d+-\d+-\d+.*?<\/div>', response.text)[0]
        item['time'] = re.findall(r'<div class="c-article__author">.*? · (\d+-\d+-\d+).*?<\/div>', response.text)[0]
        content = re.findall(r'<div class="c-article__summary-text">([\s\S]*?)<div class="c-article__keywords">', response.text)[0]
        content = Tool.filter_tags(content)
        item['content'] = content
        print('====================================================================================================')
        yield item
