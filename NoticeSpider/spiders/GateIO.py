# -*- coding: utf-8 -*-
import scrapy


class GateioSpider(scrapy.Spider):
    name = "GateIO"
    allowed_domains = ["gate.io"]
    start_urls = (
        'http://www.gate.io/',
    )

    def parse(self, response):
        pass
