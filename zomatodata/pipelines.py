import csv
from items import Restaurant

class CSVPipeline(object):
    def __init__(self):
        names = Restaurant().fields
        self.csv_file = open('res.csv', 'wb')
        self.file = csv.DictWriter(self.csv_file, fieldnames=names)
        self.file.writeheader()

    def process_item(self, item, spider):
        self.file.writerow(item)

    def close_spider(self, spider):
        self.csv_file.close()