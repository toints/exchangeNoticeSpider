# -*- coding: utf-8 -*-
import scrapy


class KucoinSpider(scrapy.Spider):
    name = "Kucoin"
    allowed_domains = ["kucoin.com"]
    start_urls = (
        'http://www.kucoin.com/',
    )

    def parse(self, response):
        pass
