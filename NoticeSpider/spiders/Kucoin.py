# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import re
from hashlib import md5
import logging

from NoticeSpider.items import NoticespiderItem

class KucoinSpider(scrapy.Spider):
    name = "Kucoin"
    allowed_domains = ["kucoin.com"]
    start_urls = (
            'https://news.kucoin.com/category/%E5%85%AC%E5%91%8A/',
    )

    logger = logging.getLogger("KucoinSpider")
    host = 'https://news.kucoin.com'
    rules = (
        Rule(LinkExtractor(allow=()), callback="parse", follow=True),
    )

    def parse(self, response):
        try:
            article_list = response.xpath('//main[@id="main" and @class="site-main posts-loop" and @role="main"]/article/h2/a').extract()
            self.logger.debug(article_list)
            for i in range(0, len(article_list)):
                item = NoticespiderItem()
                url = re.findall(r'<a href="(.*?)" rel=', article_list[i], re.S)[0]
                #item['url'] = self.host + url
                #contains complete URL path
                item['url'] = url
                self.logger.info(item['url'])
                item['urlmd5'] = md5(item['url']).hexdigest()
                item['title'] = re.findall(r'<span>(.*?)</span>', article_list[i], re.S)[0]
                self.logger.info('ITEM--> url:%s, urlmd5:%s, title:%s',item['url'], item['urlmd5'], item['title'])
                yield item
        except Exception,e:
            self.logger.critical(e)

