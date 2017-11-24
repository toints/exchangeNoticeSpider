# -*- coding: utf-8 -*-
import scrapy


class OkexSpider(scrapy.Spider):
    name = "OKex"
    allowed_domains = ["okex.com"]
    start_urls = (
        'http://www.okex.com/',
    )

    def parse(self, response):
        pass
