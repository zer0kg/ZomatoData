import re

class CostPipeline(object):
    def process_item(self, item, spider):
        cost = item['cost']
        try:
            item['cost'] = int(re.sub('[^0-9]+', '', cost))
        except ValueError:
            item['cost'] = 'NA'
        return item
