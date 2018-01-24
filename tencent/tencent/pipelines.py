# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# 写到数据库
# import sqlite3
# class TencentPipeline(object):
#     def open_spider(self,spider):
#         self.con = sqlite3.connect('tencent.sqlite')
#         self.cu = self.con.cursor()
#     def process_item(self, item, spider):
#         tencent_insert = "insert into tencent (title,type,num,position,time) values('{}','{}','{}','{}','{}')".format(item['title'],item['type'],item['num'],item['position'],item['time'])
#         self.cu.execute(tencent_insert)
#         self.con.commit()
#         return item
#     def close_spider(self,spider):
#         self.con.close()
# 写到本地txt文件
class TencentPipeline2(object):
    def __init__(self):
        self.f = open('neiwen.txt','w')
    def process_item(self, item, spider):
        content = item['tou'] + item['content']
        self.f.write(content)
        return item
    def close_spider(self,spider):
        self.f.close()