# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import re
from hashlib import md5
import logging

from scrapy.http import Request, FormRequest
from NoticeSpider.items import NoticespiderItem

class BcexSpider(scrapy.Spider):
    name = "Bcex"
    allowed_domains = ["bcex.ca"]
    logger = logging.getLogger("BcexSpider")
    host = 'https://www.bcex.ca'
    start_urls = (
            'https://www.bcex.ca/news/',
    )
    rules = (
        Rule(LinkExtractor(allow=()), callback="start_requests", follow=True),
    )

    def start_requests(self):
        headers = {'Set-Cookie':'lang=zh_CN', 'Cookie':'lang=zh_CN'}
        for i,url in enumerate(self.start_urls):
            yield Request(url, callback=self.parse_item, headers=headers)

    def parse_item(self, response):
        try:
            self.logger.debug(response.headers)
            article_list = response.xpath('//ul[@id="list"]/li/a').extract()
            self.logger.debug(article_list)
            for i in range(0, len(article_list)):
                item = NoticespiderItem()
                url = re.findall(r'<a href="(.*?)"', article_list[i], re.S)[0]
                item['url'] = self.host + url
                self.logger.info(item['url'])
                item['urlmd5'] = md5(item['url']).hexdigest()
                #Do not delete any space in the regex
                item['title'] = re.findall(r'</span>\n                        (.*?)                    </a>', article_list[i], re.S)[0]
                self.logger.info('ITEM--> url:%s, urlmd5:%s, title:%s',item['url'], item['urlmd5'], item['title'])
                yield item
        except Exception,e:
            self.logger.critical(e)
