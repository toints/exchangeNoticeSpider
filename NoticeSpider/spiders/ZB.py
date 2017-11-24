# -*- coding: utf-8 -*-
import scrapy


class ZbSpider(scrapy.Spider):
    name = "ZB"
    allowed_domains = ["zb.com"]
    start_urls = (
        'http://www.zb.com/',
    )

    def parse(self, response):
        pass
