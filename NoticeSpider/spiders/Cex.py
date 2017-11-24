# -*- coding: utf-8 -*-
import scrapy


class CexSpider(scrapy.Spider):
    name = "Cex"
    allowed_domains = ["cex.io"]
    start_urls = (
        'http://www.cex.io/',
    )

    def parse(self, response):
        pass
