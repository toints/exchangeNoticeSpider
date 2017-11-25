# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import re
from hashlib import md5
import logging

from NoticeSpider.items import NoticespiderItem

class BtccSpider(scrapy.Spider):
    name = "Btcc"
    allowed_domains = ["btcc.com"]
    start_urls = (
        'https://www.btcc.com/news/zh/newsletters/',
    )
    logger = logging.getLogger("BtccSpider")
    host = 'https://www.btcc.com'
    rules = (
        Rule(LinkExtractor(allow=()), callback="parse", follow=True),
    )

    def parse(self, response):
        try:
            article_list = response.xpath('//div[@class="container"]/div[@class="news-preview-wrap col-sm-6 col-md-4"]/a').extract()
            self.logger.debug(article_list)
            for i in range(0, len(article_list)):
                item = NoticespiderItem()
                url = re.findall(r'<a class="news-preview-link" href="(.*?)"', article_list[i], re.S)[0]
                item['url'] = self.host + url
                self.logger.info(item['url'])
                item['urlmd5'] = md5(item['url']).hexdigest()
                item['title'] = re.findall(r'<h2 class="post-title news-preview-content-title">(.*?)</h2>', article_list[i], re.S)[0]
                self.logger.info('ITEM--> url:%s, urlmd5:%s, title:%s',item['url'], item['urlmd5'], item['title'])
                yield item
        except Exception,e:
            self.logger.critical(e)

