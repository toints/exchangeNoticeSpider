# -*- coding: utf-8 -*-
import scrapy


class BigoneSpider(scrapy.Spider):
    name = "BigOne"
    allowed_domains = ["big.one"]
    start_urls = (
        'http://www.big.one/',
    )

    def parse(self, response):
        pass
