# -*- coding: utf-8 -*-
import scrapy


class Btc018Spider(scrapy.Spider):
    name = "Btc018"
    allowed_domains = ["btc018.com"]
    start_urls = (
        'http://www.btc018.com/',
    )

    def parse(self, response):
        pass
