# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import re
from hashlib import md5
import logging

from NoticeSpider.items import NoticespiderItem


class HuobiproSpider(scrapy.Spider):
    name = "HuobiPro"
    host = "https://www.huobi.pro"
    allowed_domains = ["huobi.pro"]
    start_urls = (
            'https://www.huobi.pro/zh-cn/notice/',
    )
    logger = logging.getLogger("HuobiproSpider")

    rules = (
            Rule(LinkExtractor(allow=(r'/zh-cn/notice/')), callback="parse", follow=True),
            )

    def parse(self, response):
        try:
            article_list = response.xpath('//ul[@class="page_notice_list_content"]/li/a').extract()
            self.logger.debug(article_list)
            for i in range(0, len(article_list)):
                item = NoticespiderItem()
                url = re.findall(r'<a href="(.*?)">', article_list[i], re.S)[0]
                item['url'] = self.host + url
                item['urlmd5'] = md5(item['url']).hexdigest()
                item['title'] = re.findall(r'<h2 class="page_notice_title">(.*?)</h2>', article_list[i], re.S)[0]
                self.logger.info('ITEM--> url:%s, urlmd5:%s, title:%s',item['url'], item['urlmd5'], item['title'])
                return
                yield item
        except Exception,e:
            self.logger.critical(e)
