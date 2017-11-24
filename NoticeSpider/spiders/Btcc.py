# -*- coding: utf-8 -*-
import scrapy


class BtccSpider(scrapy.Spider):
    name = "Btcc"
    allowed_domains = ["btcc.com"]
    start_urls = (
        'http://www.btcc.com/',
    )

    def parse(self, response):
        pass
