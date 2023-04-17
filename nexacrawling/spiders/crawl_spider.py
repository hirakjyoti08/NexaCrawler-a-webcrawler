from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class CrawlingSpider(CrawlSpider):
    name = "comecrawler"
    allow_domains = ["toscrape.com"]
    start_urls = ["http://books.toscrape.com/"]

    PROXY_SERVER = "50.63.165.137"  # https://geonode.com/free-proxy-list
  
   #crawling here
    rules = (
        Rule(LinkExtractor(allow="catalogue/category")),
        Rule(LinkExtractor(allow="catalogue", deny ="category"), callback="parse_item")
    )
   
   #extract the tittle and price of the item from thw website
    def parse_item(self, response):
        yield{
            "title": response.css(".product_main h1::text").get(),
            "price": response.css(".price_color::text").get(),
            "availability": response.css(".availability::text")[1].get().replace("\n","").replace(" ","")
        }
    