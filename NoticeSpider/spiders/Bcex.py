# -*- coding: utf-8 -*-
import scrapy


class BcexSpider(scrapy.Spider):
    name = "Bcex"
    allowed_domains = ["bcex.ca"]
    start_urls = (
        'http://www.bcex.ca/',
    )

    def parse(self, response):
        pass
