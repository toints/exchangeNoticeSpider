# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import re
from hashlib import md5
import logging

from NoticeSpider.items import NoticespiderItem

class BinanceSpider(CrawlSpider):
    logger = logging.getLogger("BinanceSpider")
    name = "Binance"
    host = 'https://support.binance.com'
    allowed_domains = ["binance.com"]
    start_urls = (
            'https://support.binance.com/hc/zh-cn/sections/115000106672-%E6%96%B0%E5%B8%81%E4%B8%8A%E7%BA%BF',
            'https://support.binance.com/hc/zh-cn/sections/115000202591-%E6%9C%80%E6%96%B0%E5%85%AC%E5%91%8A'
    )

    rules = (
        Rule(LinkExtractor(allow=(r'/hc/zh-cn/sections/115000106672-\u65b0\u5e01\u4e0a\u7ebf$')), callback="parse", follow=True),
        Rule(LinkExtractor(allow=(r'/hc/zh-cn/sections/115000202591-\u6700\u65b0\u516c\u544a$')), callback="parse", follow=True),
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


