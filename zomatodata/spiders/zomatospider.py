import scrapy
from scrapy.spiders import Spider
from re import findall

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

        next_link = response.css('li.current + li.active a').xpath('@href').extract()
        print "\n\nNEXT LINK:", next_link
        if next_link:
            yield scrapy.Request(response.urljoin(next_link[0]), callback=self.parse)

    def parse_rest(self, response):
        rest = Restaurant()

        rest['r_name'] = response.xpath('//h1/a/span/text()').extract()[0]
        rest['r_id'] = response.xpath('//*/@data-res-id').extract()[0]
        rest['r_type'] = response.css('div.res-info-estabs > a::text').extract()[0]
        rest['link'] = response.url
        rest['city'] = findall('\\.com\/([a-z]+)\/', rest['link'])[0]
        rest['cost'] = response.css('span[itemprop="priceRange"]::text').extract()[0]
        rest['area'] = response.css('span[itemprop="addressLocality"]::text').extract()[0]
        rest['rating'] = response.css('div[itemprop="ratingValue"]::text').extract()
        rest['rating_votes'] = response.css("span[itemprop='ratingCount']::text").extract()
        rest['reviews'] = response.css("div.res-main-stats-num::text").extract()
        rest['photos'] = response.css("div#ph_count::text").extract()
        rest['bookmarks'] = response.css("div#wtt_count::text").extract()
        rest['checkins'] = response.css("div#bt_count::text").extract()
        rest['cuisines'] = response.css("a[itemprop='servesCuisine']::text").extract()
        rest['collections'] = response.css("span.res-page-collection-text > a::text").extract()
        rest['r_postcode'] = response.css("span[itemprop='postalCode']::text").extract()
        rest['r_address'] = response.css("div.res-main-address-text::text").extract()
        rest['r_latitude'] = response.selector.re("\|([\d.]+),([\d.]+)\|")
        yield rest
