import re

class CostPipeline(object):
    def process_item(self, item, spider):
        cost = item['cost']
        try:
            item['cost'] = int(re.sub('[^0-9]+', '', cost))
            print "PART REACHED"
        except ValueError:
            item['cost'] = 'NA'
        return item

class RatingPipeline(object):
    def process_item(self, item, spider):
        try:
            item['rating'] = int(item['rating'].strip())
        except ValueError:
            item['rating'] = 'NA'
        return item
