#!/usr/bin/env python
#-*- coding:utf-8 -*-

#from scrapy import cmdline
#cmdline.execute("scrapy crawl BinanceSpider".split())

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

process = CrawlerProcess(get_project_settings())

#process.crawl('Binance', domain='binance.com')
#process.crawl('OKex', domain='okex.com')
process.crawl('HuobiPro', domain='huobi.pro')
process.start()
