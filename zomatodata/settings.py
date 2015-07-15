SPIDER_MODULES = ['zomatodata.spiders']
NEWSPIDER_MODULE = 'zomatodata.spiders'
DEFAULT_ITEM_CLASS = 'zomatodata.items.Restaurant'

ITEM_PIPELINES = {
    'zomatodata.pipelines.CostPipeline': 300,
    'zomatodata.pipelines.RatingPipeline': 400
}
