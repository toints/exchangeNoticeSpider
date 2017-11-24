# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors.sgml import SgmlLinkExtractor
from scrapy.linkextractors import LinkExtractor
from scrapy.http import Request
import re
import time
from hashlib import md5

from NoticeSpider.items import NoticespiderItem
from scrapy.conf import settings

class BinanceSpider(scrapy.Spider):
    name = "Binance"
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
            article_list = response.xpath('//ul[@class="article-list"]')
            self.log.info('------ start article list ---------')
            self.log.info(article_list)
            self.log.info('------ end article list ---------')
            for article in article_list:
                item = NoticespiderItem()
                item['url'] = article.xpath('li/a/@href')
                item['urlmd5'] = md5(item['url']).hexdigest()
                item['title'] = article.xpath('li/a/text()').extract()
                self.log.info('ITEM--> url:%s, urlmd5:%s, title:%s' %(item['url'], item['urlmd5'], item['title']))
                yield item
        except Exception,e:
            self.log.exception(e)

