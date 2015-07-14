from scrapy.spider import Spider
from scrapy.selector import Selector

from zomatodata.items import Restaurant

s = Restaurant()


class ZomatoSpider(Spider):
    name = 'zomatospider'
    allowed_domains = ['zomato.com']
    start_urls = [
        'https://www.zomato.com/chennai/restaurants?page=1',
        'https://www.zomato.com/bangalore/restaurants?page=1',
        'https://www.zomato.com/mysore/restaurants?page=1',
        'https://www.zomato.com/pune/restaurants?page=1',
        'https://www.zomato.com/mumbai/restaurants?page=1',
        'https://www.zomato.com/hyderabad/restaurants?page=1',
        'https://www.zomato.com/kolkata/restaurants?page=1',
        'https://www.zomato.com/ncr/restaurants?page=1',
    ]

