import scrapy
import json
# div.post-header > h2 > a
# //*[@id="hs_cos_wrapper_module_1523032069834331"]/div/div/div/div/div[1]/div[10]/div[2]/h2/a


class WatchSpider(scrapy.Spider):
    name = 'chemaSpider'
    start_urls = ['https://www.elladodelmal.com/']
    page_n = 0
    article_n = 0
    
    def parse(self, response):
        for article in response.css('#Blog1 > div.blog-posts.hfeed > div'):
            title = article.css('div > div > div > h3 > a ::text').extract_first()
            content = article.css('div > div > div > div.post-body ::text').extract_first()
            print(f"Fetched article N: {self.article_n}")
            self.article_n += 1
            print("{} && {}".format(title, content))
            

        for next_page in response.css('#blog-pager-older-link a'):
            if self.page_n > 5:
                break
            self.page_n += 1
            yield response.follow(next_page, self.parse)



from scrapy.crawler import CrawlerProcess

# optional
process = CrawlerProcess({
    'USER_AGENT': 'Google SEO BOT'
})

process.crawl(WatchSpider)
process.start()