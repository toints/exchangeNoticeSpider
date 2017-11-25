# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import re
from hashlib import md5
import logging

from NoticeSpider.items import NoticespiderItem

class CoinwSpider(scrapy.Spider):
    name = "Coinw"
    allowed_domains = ["coinw.com"]
    start_urls = (
            'https://www.coinw.com/newService/ourService.html?id=1',
    )

    logger = logging.getLogger("CoinwSpider")
    host = 'https://www.coinw.com'
    rules = (
        Rule(LinkExtractor(allow=()), callback="parse", follow=True),
    )

    def parse(self, response):
        try:
            article_list = response.xpath('//div[@class="news-list bg-color-white mb20"]/div/div/div/div/div[2]/div[1]/a').extract()
            self.logger.debug(article_list)
            for i in range(0, len(article_list)):
                item = NoticespiderItem()
                url = re.findall(r'<a href="(.*?)" class="', article_list[i], re.S)[0]
                item['url'] = self.host + url
                self.logger.info(item['url'])
                item['urlmd5'] = md5(item['url']).hexdigest()
                item['title'] = re.findall(r'class="link-1">(.*?)</a>', article_list[i], re.S)[0]
                self.logger.info('ITEM--> url:%s, urlmd5:%s, title:%s',item['url'], item['urlmd5'], item['title'])
                yield item
        except Exception,e:
            self.logger.critical(e)


