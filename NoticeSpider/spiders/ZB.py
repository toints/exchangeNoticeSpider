# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import re
from hashlib import md5
import logging

from NoticeSpider.items import NoticespiderItem

class ZBSpider(scrapy.Spider):
    name = "ZB"
    allowed_domains = ["zb.com"]
    start_urls = (
        'https://www.zb.com/i/blog',
    )

    logger = logging.getLogger("ZBSpider")
    host = 'https://www.zb.com'
    rules = (
        Rule(LinkExtractor(allow=()), callback="parse", follow=True),
    )

    def parse(self, response):
        try:
            article_list = response.xpath('//ul[@class="cbp_tmtimeline"]/li/div[@class="cbp_tmlabel"]/article/header/h3/a').extract()
            self.logger.debug(article_list)
            for i in range(0, len(article_list)):
                item = NoticespiderItem()
                url = re.findall(r'<a href="(.*?)" target=', article_list[i], re.S)[0]
                #replace '&' to ''
                rep_url = url.replace('amp;', '')
                item['url'] = self.host + rep_url
                self.logger.info(item['url'])
                item['urlmd5'] = md5(item['url']).hexdigest()
                item['title'] = re.findall(r'_blank">(.*?)\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t</a>', article_list[i], re.S)[0]
                self.logger.info('ITEM--> url:%s, urlmd5:%s, title:%s',item['url'], item['urlmd5'], item['title'])
                yield item
        except Exception,e:
            self.logger.critical(e)

