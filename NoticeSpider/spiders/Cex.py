# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import re
from hashlib import md5
import logging

from NoticeSpider.items import NoticespiderItem

class CexSpider(scrapy.Spider):
    name = "Cex"
    allowed_domains = ["cex.com"]
    start_urls = (
        'https://www.cex.com/Art/index/id/1.html',
    )
    logger = logging.getLogger("CexSpider")
    host = 'https://www.cex.com'
    rules = (
        Rule(LinkExtractor(allow=()), callback="parse", follow=True),
    )

    def parse(self, response):
        try:
            article_list = response.xpath('//table[@class="table table-hover table-striped"]/tbody/tr/td/a').extract()
            self.logger.debug(article_list)
            for i in range(0, len(article_list)):
                item = NoticespiderItem()
                url = re.findall(r'<a class="pull-left" href="(.*?)"', article_list[i], re.S)[0]
                item['url'] = self.host + url
                self.logger.info(item['url'])
                item['urlmd5'] = md5(item['url']).hexdigest()
                item['title'] = re.findall(r'">\r\n\t\t\t\t\t\t\t\t(.*?)\t\t\t\t\t\t\t\t</a>', article_list[i], re.S)[0]
                self.logger.info('ITEM--> url:%s, urlmd5:%s, title:%s',item['url'], item['urlmd5'], item['title'])
                yield item
        except Exception,e:
            self.logger.critical(e)

