help:
	@echo	"make genall	-- generate all spiders"
	@echo	"make run	-- run all spiders"
	@echo	"make runDeamon	-- run all spiders in deamon"
	@echo	"make copy	-- copy source code to github path"


copy:
	cp -rf ./* /data/develop/exchangeNoticeSpider/

genall:
	scrapy genspider Binance binance.com
	scrapy genspider OKex okex.com
	scrapy genspider GateIO gate.io
	scrapy genspider Chaoex chaoex.com
	scrapy genspider Kucoin kucoin.com
	scrapy genspider BigOne big.one
	scrapy genspider Cex cex.io
	scrapy genspider HuobiPro huobi.pro
	scrapy genspider Aex aex.com
	scrapy genspider Btcc btcc.com
	scrapy genspider Allcoin allcoin.com
	scrapy genspider Bcex bcex.ca
	scrapy genspider ZB zb.com
	scrapy genspider Btc018 btc018.com    

run:
	python run.py 

runDeamon:
	nohup python run.py &
