# -*- coding: utf-8 -*-
import scrapy
import re
from zbbnews import Tool


class Zbbxw1Spider(scrapy.Spider):
    name = 'zbbxw1'
    allowed_domains = ['www.chinaipo.com']
    start_urls = ['http://www.chinaipo.com/news/128324.html']

    def parse(self, response):
        item = {}
        item['title'] = re.findall(r'<h1 class="c-article__title">(.*?)<\/h1>', response.text)[0]
        item['author'] = re.findall(r'<div class="c-article__author">(.*?) · \d+-\d+-\d+.*?<\/div>', response.text)[0]
        item['time'] = re.findall(r'<div class="c-article__author">.*? · (\d+-\d+-\d+).*?<\/div>', response.text)[0]
        content = \
        re.findall(r'<div class="c-article__summary-text">([\s\S]*?)<div class="c-article__keywords">', response.text)[
            0]
        content = Tool.filter_tags(content)
        item['content'] = content
        print('====================================================================================================')
        yield item