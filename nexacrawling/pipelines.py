# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

#this is the main pipeline
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class NexacrawlingPipeline:
    def process_item(self, item, spider):
        return item
