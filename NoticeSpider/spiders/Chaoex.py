# -*- coding: utf-8 -*-
import scrapy


class ChaoexSpider(scrapy.Spider):
    name = "Chaoex"
    allowed_domains = ["chaoex.com"]
    start_urls = (
        'http://www.chaoex.com/',
    )

    def parse(self, response):
        pass
