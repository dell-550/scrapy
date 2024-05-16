# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class VideospiderPipeline:
    def open_spider(self, spider):
        self.file = open("data.csv", "a", encoding='utf-8')

    def close_spider(self, spider):
        if self.file:
            self.file.close()

    def process_item(self, item, spider):
        item['score'] = item['score'].replace("\n", "")
        item['downloadurl'] = ' '.join(item['downloadurl'])
        datas = dict(item)
        data = json.dumps(datas, ensure_ascii=False)
        print(data)
        self.file.write(data)
        self.file.write('\n')
        return item
