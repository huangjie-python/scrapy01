# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import re
from jxbbs import Tool


class JxltSpider(CrawlSpider):
    name = 'jxlt'
    allowed_domains = ['jxbbs.com.cn']
    start_urls = ['http://www.jxbbs.com.cn/']

    rules = (
        Rule(LinkExtractor(allow=r'http:\/\/www\.jxbbs\.com\.cn\/forum\.php\?mod=forumdisplay&fid=\d+.*?'),  follow=True),
        Rule(LinkExtractor(allow=r'http:\/\/www\.jxbbs\.com\.cn\/forum\.php\?mod=viewthread&tid=\d+'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        response = response.text
        item = {}
        tiezilist = []
        title = re.findall(r'<span id="thread_subject">(.*?)<\/span>', response)
        item['title'] = title[0]
        tzs = re.findall(r'<div id="post_\d+".*?>([\s\S]*?<div id="comment_\d+" class="cm">)', response)
        for tz in tzs:
            tiezi = {}
            tiezi['author'] = re.findall(r'<a href=".*?".*?class=".*?author">(.*?)<\/a>',tz)[0]
            tiezi['time'] = re.findall(r'发表于 (.*?)<\/em>',tz)[0]
            content = re.findall(r'<div class="t_fsz">([\s\S]*?)<div id="comment_\d+" class="cm">',tz)[0]
            content = Tool.filter_tags(content)
            tiezi['content'] = content
            tiezilist.append(tiezi)
        item['tiezi'] = tiezilist
        yield item
