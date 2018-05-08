# -*- coding: utf-8 -*-
from scrapy.pipelines.images import ImagesPipeline

import MySQLdb
import MySQLdb.cursors
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


# class FilmspiderPipeline(object):
#     def process_item(self, item, spider):
#         return item
class FilmImagePipeline(ImagesPipeline):
    def item_completed(self, results, item, info):
        if "front_image_url" in item:
            for ok, value in results:
                image_file_path = value["path"]
            item["front_image_path"] = image_file_path

        return item


class MysqlPipeline(object):
    def __init__(self):
        self.conn = MySQLdb.connect('127.0.0.1', 'root', 'cl951120', 'CLOnline', charset="utf8", use_unicode=True)
        self.cursor=self.conn.cursor()
    def process_item(self,item,spider):
        insert_sql = """
                    insert into article_film_article(title, url, url_object_id, create_date,front_image_url,article,front_image_name)
                    VALUES (%s, %s, %s, %s, %s,%s,%s)
                """
        self.cursor.execute(insert_sql,(item["title"],item["url"],item["url_object_id"],item["create_date"],item["front_image_url"],item["article"],item["front_image_name"]))
        self.conn.commit()