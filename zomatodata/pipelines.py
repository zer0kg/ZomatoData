import re
import csv
from items import Restaurant

class CostPipeline(object):
    def process_item(self, item, spider):
        try:
            item['cost'] = int(re.sub('[^0-9]+', '', item['cost'][0]))
        except ValueError or IndexError:
            item['cost'] = 'NA'
        return item

class RatingPipeline(object):
    def process_item(self, item, spider):
        # print "RATING =", item['rating']
        try:
            item['rating'] = item['rating'][0]
            item['rating'] = float(item['rating'].strip())
        except ValueError or IndexError:
            item['rating'] = 'NA'
        return item

class PostalCodePipeline(object):
    def process_item(self, item, spider):
        if len(item['r_postcode']) == 0:
            item['r_postcode'] = 'NA'
        else:
            item['r_postcode'] = int(item['r_postcode'][0])

        return item

class AddressPipeline(object):
    def process_item(self, item, spider):
        add = ''.join(map(lambda x: x.strip(), item['r_address']))
        item['r_address'] = add
        return item

class OtherInfoPipeline(object):
    def process_item(self, item, spider):
        try:
            item['bookmarks'] = int(item['bookmarks'][0])
        except ValueError or IndexError:
            item['bookmarks'] = 'NA'

        try:
            item['checkins'] = int(item['checkins'][0])
        except ValueError or IndexError:
            item['checkins'] = 'NA'

        try:
            item['photos'] = int(item['photos'][0])
        except ValueError or IndexError:
            item['photos'] = 'NA'

        try:
            item['reviews'] = int(item['reviews'][0])
        except ValueError or IndexError:
            item['reviews'] = 'NA'

        try:
            item['rating_votes'] = int(item['rating_votes'][0])
        except ValueError or IndexError:
            item['rating_votes'] = 'NA'
        return item

class LocationPipeline(object):
    def process_item(self, item, spider):
        l = len(item['r_latitude'])
        if l == 0:
            item['r_latitude'] = 'NA'
            item['r_longitude'] = 'NA'
        elif l != 0:
            item['r_latitude'], item['r_longitude'] = map(float, item['r_latitude'])

        return item

class CSVPipeline(object):
    def __init__(self):
        names = Restaurant.keys()
        self.csv_file = open('res.csv', 'w')
        self.file = csv.DictWriter(self.csv_file, fieldnames=names)
        self.file.writeheader()

    def process_item(self, item, spider):
        self.file.writerow(item)

    def close_spider(self, spider):
        self.csv_file.close()