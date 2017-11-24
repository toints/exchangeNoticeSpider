# -*- coding: utf-8 -*-
import scrapy


class HuobiproSpider(scrapy.Spider):
    name = "HuobiPro"
    allowed_domains = ["huobi.pro"]
    start_urls = (
        'http://www.huobi.pro/',
    )

    def parse(self, response):
        pass
