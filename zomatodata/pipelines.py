import re
import csv
from items import Restaurant
import unicodedata


def unicode_convert(s):
    return unicodedata.normalize('NFKD', s).encode('ascii', 'ignore')

class CSVPipeline(object):
    def __init__(self):
        names = Restaurant().fields
        self.csv_file = open('res.csv', 'w')
        self.file = csv.DictWriter(self.csv_file, fieldnames=names)
        self.file.writeheader()

    def process_item(self, item, spider):
        self.file.writerow(item)

    def close_spider(self, spider):
        self.csv_file.close()