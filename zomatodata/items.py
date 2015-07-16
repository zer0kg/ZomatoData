from scrapy.item import Item, Field

class Restaurant(Item):

    r_name = Field()
    r_id = Field()
    r_type = Field()
    r_postcode = Field()
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