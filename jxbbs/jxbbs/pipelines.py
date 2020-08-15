# -*- coding: utf-8 -*-
import json
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class JxbbsPipeline(object):
    def process_item(self, item, spider):
        # print('========================开始写入==============================')
        # tiezi = json.dumps(item)
        # with open('jxlttzs.json','w', encoding='utf-8') as f:
        #     f.write(tiezi)

        title = item['title']
        tzlist = item['tiezi']
        tzs = 'tiezi['
        for tz in tzlist:
            tzs += 'author: ' + tz['author'] + '。time' + tz['time'] + '。content' + tz['content'] + '。\n'
        tzs += ']'
        print('========================开始写入==============================')
        with open('jxlttzs.txt', 'a', encoding='utf-8') as f:
            f.write("title:" + title + "。tiezi:" + tzs + '\n')
        return item
