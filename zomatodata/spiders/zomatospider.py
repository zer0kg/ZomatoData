import scrapy
from scrapy.spiders import Spider
from scrapy.selector import Selector

from zomatodata.items import Restaurant


class ZomatoSpider(Spider):
    name = 'zomatospider'
    allowed_domains = ['zomato.com']
    start_urls = [
        'https://www.zomato.com/chennai/restaurants?page=1',
        # 'https://www.zomato.com/bangalore/restaurants?page=1',
        # 'https://www.zomato.com/mysore/restaurants?page=1',
        # 'https://www.zomato.com/pune/restaurants?page=1',
        # 'https://www.zomato.com/mumbai/restaurants?page=1',
        # 'https://www.zomato.com/hyderabad/restaurants?page=1',
        # 'https://www.zomato.com/kolkata/restaurants?page=1',
        # 'https://www.zomato.com/ncr/restaurants?page=1',
    ]

    def parse(self, response):
        for rest in response.css('a.result-title'):
            url = rest.xpath('@href').extract()[0]
            yield scrapy.Request(url, callback=self.parse_rest)

        # next_link = response.css('ul.paginator-control > li.current + li.active').xpath('a/@href')
        # if next_link:
        #     yield scrapy.Request(next_link.extract()[0], callback=self.parse)

    def parse_rest(self, response):
        rest = Restaurant()

        rest['r_name'] = response.xpath('//h1/a/span/text()').extract()[0]
        rest['r_id'] = response.xpath('//*/@data-res-id').extract()[0]
        print rest
