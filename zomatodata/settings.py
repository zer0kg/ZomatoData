SPIDER_MODULES = ['zomatodata.spiders']
NEWSPIDER_MODULE = 'zomatodata.spiders'
DEFAULT_ITEM_CLASS = 'zomatodata.items.Restaurant'

ITEM_PIPELINES = {
    'zomatodata.pipelines.CostPipeline': 300,
    'zomatodata.pipelines.RatingPipeline': 400,
    'zomatodata.pipelines.PostalCodePipeline': 500,
    'zomatodata.pipelines.AddressPipeline': 600,
    'zomatodata.pipelines.OtherInfoPipeline': 700,
    'zomatodata.pipelines.LocationPipeline': 800,
    'zomatodata.pipelines.CSVPipeline': 1000
}
