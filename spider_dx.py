import scrapy
import json
from scrapy.crawler import CrawlerProcess


class WatchSpider(scrapy.Spider):
    name = 'chemaSpider'
    start_urls = ['https://www.dx.com/c/phones-telecommunications-18/mobile-phone-accessories-parts-1800162/mobile-phone-chargers-3741']
    article_n = 0
    
    def parse(self, response):
        for article in response.css('div#proList > ul.product-list'):
            #title = article.css('div.product-list-item::text').extract_first()
            title = article.css('li > div::text').extract_first()  

            print("-----------------------------------")
            print(f"Fetched article N: {self.article_n}")
            print(f"{title}")    
            print("-----------------------------------")

            self.article_n += 1



process = CrawlerProcess({
    'USER_AGENT': 'Google SEO BOT'
})

process.crawl(WatchSpider)
process.start()