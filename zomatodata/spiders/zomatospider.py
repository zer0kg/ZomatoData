import scrapy
from scrapy.spiders import Spider
from re import findall
from zomatodata.items import Restaurant
from zomatodata.items import RestItemLoader

class ZomatoSpider(Spider):
    name = 'zomatospider'
    allowed_domains = ['zomato.com']
    start_urls = [
        'https://www.zomato.com/chennai/restaurants?page=105',
        # 'https://www.zomato.com/bangalore/restaurants?page=1',
        # 'https://www.zomato.com/mysore/restaurants?page=1',
        # 'https://www.zomato.com/pune/restaurants?page=1',
        # 'https://www.zomato.com/mumbai/restaurants?page=1',
        # 'https://www.zomato.com/hyderabad/restaurants?page=1',
        # 'https://www.zomato.com/kolkata/restaurants?page=1',
        # 'https://www.zomato.com/ncr/restaurants?page=1',
    ]


    def parse(self, response):
        global COUNT
        for rest in response.css('a.result-title'):
            url = rest.xpath('@href').extract()[0]
            yield scrapy.Request(url, callback=self.parse_rest)

        next_link = response.css('li.current + li.active a').xpath('@href').extract()
        print "NEXT LINK:", next_link
        if next_link:
            yield scrapy.Request(response.urljoin(next_link[0]), callback=self.parse)

    def parse_rest(self, response):
        rest = RestItemLoader(item=Restaurant(), response=response)

        rest.add_xpath('r_name', '//h1/a/span/text()')
        rest.add_xpath('r_id', '//*/@data-res-id')
        rest.add_css('r_type', 'div.res-info-estabs > a::text')
        rest.add_value('link', response.url)
        rest.add_value('city',  findall('\\.com\/([a-z]+)\/', rest.get_value('link')))
        rest.add_css('cost', 'span[itemprop="priceRange"]::text')
        rest.add_css('area', 'span[itemprop="addressLocality"]::text')
        rest.add_css('rating', 'div[itemprop="ratingValue"]::text')
        rest.add_css('rating_votes', "span[itemprop='ratingCount']::text")
        rest.add_css('reviews', "div.res-main-stats-num::text")
        rest.add_css('photos', "div#ph_count::text")
        rest.add_css('bookmarks', "div#wtt_count::text")
        rest.add_css('checkins', "div#bt_count::text")
        rest.add_css('cuisines', "a[itemprop='servesCuisine']::text")
        rest.add_css('collections', "span.res-page-collection-text > a::text")
        rest.add_css('r_address', "div.res-main-address-text::text")
        rest.add_value('r_latitude', value=response.selector.re("\|([\d.]+),[\d.]+\|"))
        rest.add_value('r_longitude', value=response.selector.re("\|[\d.]+,([\d.]+)\|"))

        yield rest.load_item()




