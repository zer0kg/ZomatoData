SPIDER_MODULES = ['zomatodata.spiders']
NEWSPIDER_MODULE = 'zomatodata.spiders'
DEFAULT_ITEM_CLASS = 'zomatodata.items.Restaurant'

ITEM_PIPELINES = {
    'zomatospider.pipelines.CostPipeline': 1
}