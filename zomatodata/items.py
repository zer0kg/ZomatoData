from scrapy.item import Item, Field
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose
import unicodedata
import re

# TODO: Rewrite the below class to include Item Loaders

class Restaurant(Item):

    r_name = Field()
    r_id = Field()
    r_type = Field()
    r_address = Field()
    city = Field()
    link = Field()
    cost = Field()
    area = Field()
    rating = Field()
    rating_votes = Field()
    reviews = Field()
    photos = Field()
    bookmarks = Field()
    checkins = Field()
    cuisines = Field()
    collections = Field()
    r_latitude = Field()
    r_longitude = Field()

def unicode_convert(s):
    return unicodedata.normalize('NFKD', s).encode('ascii', 'ignore')

class RestItem(ItemLoader):
    default_input_processor = MapCompose(unicode_convert)
    default_output_processor = TakeFirst()

    r_id_in = MapCompose(int)

    cost_in = MapCompose(lambda x: re.sub('[^0-9]+', '', x), int)

    area_in = MapCompose()



