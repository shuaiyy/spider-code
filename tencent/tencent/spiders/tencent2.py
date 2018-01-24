# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import TencentItem

class Tencent2Spider(CrawlSpider):
    name = 'tencent2'
    allowed_domains = ['tencent.com']
    start_urls = ['https://hr.tencent.com/position.php?&start=0']

    rules = (
        # Rule(LinkExtractor(allow=r'start=\d+'), callback='parse_item', follow=True),
    Rule(LinkExtractor(allow=r'detail'),callback='parse_title',follow=False),)

    # def parse_item(self, response):
    #     tc = TencentItem()
    #     xpaths = response.xpath('//tr[@class="odd"] | //tr[@class="even"]')
    #     for each in xpaths:
    #         tc['title'] = each.xpath('./td[1]/a/text()').extract()[0]
    #         tc['type'] = each.xpath('./td[2]/text()').extract()[0]
    #         tc['num'] = each.xpath('./td[3]/text()').extract()[0]
    #         tc['position'] = each.xpath('./td[4]/text()').extract()[0]
    #         tc['time'] = each.xpath('./td[5]/text()').extract()[0]
    #         yield tc
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
    def parse_title(self,response):
        tc = TencentItem()
        zifu = ''
        content = response.xpath('//ul/li/text()').extract()
        for i in content:
            zifu = zifu + i
        tou = response.xpath('//tr[@class="h"]/td/text()').extract()[0]
        tc['tou'] = tou
        tc['content'] = zifu
        yield tc