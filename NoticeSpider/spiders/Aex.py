# -*- coding: utf-8 -*-
import scrapy


class AexSpider(scrapy.Spider):
    name = "Aex"
    allowed_domains = ["aex.com"]
    start_urls = (
        'http://www.aex.com/',
    )

    def parse(self, response):
        pass
