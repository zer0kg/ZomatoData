import re

class CostPipeline(object):
    def process_item(self, item, spider):
        cost = item['cost']
        try:
            item['cost'] = int(re.sub('[^0-9]+', '', cost))
        except ValueError:
            item['cost'] = 'NA'
        return item

class RatingPipeline(object):
    def process_item(self, item, spider):
        print "RATING =", item['rating']
        try:
            item['rating'] = float(item['rating'].strip())
        except ValueError:
            item['rating'] = float('nan')
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

