# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import re
from hashlib import md5
import logging

from scrapy.http import Request, FormRequest
from NoticeSpider.items import NoticespiderItem

class AllcoinSpider(CrawlSpider):
    name = "Allcoin"
    logger = logging.getLogger("AllcoinSpider")
    host = 'https://www.allcoin.com'
    allowed_domains = ["allcoin.com"]
    start_urls = (
            'https://www.allcoin.com/Articles/Notice/',
    )
    rules = (
        Rule(LinkExtractor(allow=()), callback="start_requests", follow=True),
    )

    def start_requests(self):
        #default page is in English
        headers = {'Set-Cookie':'.culture=zh-CN; path=/; HttpOnly', 'Cookie':'.culture=zh-CN'}
        for i,url in enumerate(self.start_urls):
            self.logger.debug('****** start an request *********')
            yield Request(url, callback=self.parse_item, headers=headers)

    def parse_item(self, response):
        try:
            self.logger.debug(response.headers)
            article_list = response.xpath('//div[@id="articles-list"]/article/div/a').extract()
            self.logger.debug(article_list)
            for i in range(0, len(article_list)):
                item = NoticespiderItem()
                url = re.findall(r'<a href="(.*?)"', article_list[i], re.S)[0]
                item['url'] = self.host + url
                self.logger.info(item['url'])
                item['urlmd5'] = md5(item['url']).hexdigest()
                item['title'] = re.findall(r'<h2>(.*?)</h2>', article_list[i], re.S)[0]
                self.logger.info('ITEM--> url:%s, urlmd5:%s, title:%s',item['url'], item['urlmd5'], item['title'])
                yield item
        except Exception,e:
            self.logger.critical(e)

