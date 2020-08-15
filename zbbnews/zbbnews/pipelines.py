# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class ZbbnewsPipeline(object):
    def process_item(self, item, spider):
        # print('========================开始写入==============================')
        # tiezi = json.dumps(item)
        # with open('jbbnews.json','w', encoding='utf-8') as f:
        #     f.write(tiezi)


        news ='title:'+ item['title'] + '。author: ' + item['author'] + '。time' + item['time'] + '。content' + item['content'] + '。\n'
        print('========================开始写入==============================')
        with open('zzbnews.txt', 'a', encoding='utf-8') as f:
            f.write(news)
        return item
