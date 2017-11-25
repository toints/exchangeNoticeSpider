#!/usr/bin/env python
#-*- coding:utf-8 -*-

#from scrapy import cmdline
#cmdline.execute("scrapy crawl BinanceSpider".split())

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import time
import random

process = CrawlerProcess(get_project_settings())

while True:
    process.crawl('Binance',  domain='binance.com')
    process.crawl('OKex',     domain='okex.com')
    #process.crawl('HuobiPro', domain='huobi.pro')
    process.crawl('BigOne',   domain='big.one')
    process.crawl('Allcoin',  domain='allcoin.com')
    process.crawl('Bcex',     domain='bcex.ca')
    process.crawl('Coinw',    domain='coinw.com')
    process.crawl('Cex',      domain='cex.com')
    process.crawl('Btcc',     domain='btcc.com')
    process.crawl('GateIO',   domain='gate.io')
    process.crawl('Kucoin',   domain='kucoin.com')
    process.crawl('ZB',       domain='zb.com')
    #process.crawl('Aex',      domain='aex.com')
    #process.crawl('Chaoex',   domain='chaoex.com')
    process.start()
    time.sleep(random.randomint(270, 330))
