from scrapy.item import Item, Field
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose, Identity, Join
import unicodedata
import re

# TODO: Test ItemLoaders 

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

    rating_in = MapCompose(str.strip, float)

    rating_votes_in = MapCompose(int)
    reviews_in = MapCompose(int)
    photos_in = MapCompose(int)
    bookmarks_in = MapCompose(int)
    checkins_in = MapCompose(int)

    cuisines_out = Identity()
    collections_out = Identity()

    r_address_in = MapCompose(str.strip, unicode_convert)
    r_address_out = Join()

    r_latitude_in = MapCompose(float)
    r_longitude_in = MapCompose(float)









