# -*- coding: utf-8 -*-
import scrapy


class AllcoinSpider(scrapy.Spider):
    name = "Allcoin"
    allowed_domains = ["allcoin.com"]
    start_urls = (
        'http://www.allcoin.com/',
    )

    def parse(self, response):
        pass
