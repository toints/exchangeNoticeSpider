# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import re
from hashlib import md5
import logging

from NoticeSpider.items import NoticespiderItem

class BigoneSpider(CrawlSpider):
    logger = logging.getLogger("BigoneSpider")
    host = 'https://help.big.one'
    name = "BigOne"
    allowed_domains = ["big.one"]
    start_urls = (
            'https://help.big.one/hc/zh-tw/sections/115000476773-%E5%85%AC%E5%91%8A%E4%B8%AD%E5%BF%83',
    )

    rules = (
        Rule(LinkExtractor(allow=(r'/hc/zh-tw/sections/115000476773-\u516c\u544a\u4e2d\u5fc3$')), callback="parse", follow=True),
    )

    def parse(self, response):
        try:
            article_list = response.xpath('//ul[@class="article-list"]/li/a').extract()
            #self.logger.DEBUG(article_list)
            for i in range(0, len(article_list)):
                item = NoticespiderItem()
                url = re.findall(r'<a href="(.*?)" class="', article_list[i], re.S)[0]
                item['url'] = self.host + url
                self.logger.info(item['url'])
                item['urlmd5'] = md5(item['url']).hexdigest()
                item['title'] = re.findall(r'class="article-list-link">(.*?)</a>', article_list[i], re.S)[0]
                self.logger.info('ITEM--> url:%s, urlmd5:%s, title:%s',item['url'], item['urlmd5'], item['title'])
                yield item
        except Exception,e:
            self.logger.critical(e)

