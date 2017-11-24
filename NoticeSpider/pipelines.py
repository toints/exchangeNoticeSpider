# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem
from twisted.enterprise import adbapi
from hashlib import md5
import MySQLdb
import MySQLdb.cursors
import time
import logging

class NoticespiderPipeline(object):
    def process_item(self, item, spider):
        return item

class DuplicatesPipeline(object):
    def __init__(self):
        self.ids_seen = set()

    def process_item(self, item, spider):
        if item['urlmd5'] in self.ids_seen:
            raise DropItem('Duplicate item found:%s' %item)
        else:
            self.ids_seen.add(item['urlmd5'])
            return item

SQL_STR = {
    'INSERT_SPIDER':'''INSERT INTO mytokenSpiderInfo SET urlmd5=%s, url=%s, title=%s, createTime=%s, spider=%s'''
}
class StoreMySQLPipeline(object):
    def __init__(self, dbpool):
        self.dbpool = dbpool
        self.log = logging.getLogger("StoreMySQLPipeline")

    @classmethod
    def from_settings(cls, settings):
        dbargs = dict(
                host = settings['MYSQL_HOST'],
                db = settings['MYSQL_DBNAME'],
                user = settings['MYSQL_USER'],
                passwd = settings['MYSQL_PASSWD'],
                charset = 'utf8',
                cursorclass = MySQLdb.cursors.DictCursor,
                use_unicode=True
                )
        dbpool = adbapi.ConnectionPool('MySQLdb', **dbargs)
        return cls(dbpool)

    def process_item(self, item, spider):
        d = self.dbpool.runInteraction(self.db_insert, item, spider)
        d.addErrback(self.handle_error, item, spider)
        d.addBoth(lambda _:item)
        return d

    def db_insert(self, conn, item, spider):
        now = int(time.time())
        self.log.info('INSERT MYSQL--> urlmd5:%s, url:%s, title:%s, time:%s, spierName:%s', item['urlmd5'], item['url'], item['title'], now, spider.name)
        try:
            conn.execute(SQL_STR['INSERT_SPIDER'], (item['urlmd5'], item['url'], item['title'], now, spider.name))
        except Exception,e:
            if 'Duplicate entry' in e[1]:
                self.log.debug('******* item url:%s already in MYSQL', item['urlmd5'])
                pass
            else:
                self.log.critical(e)

    def handle_error(self, failure, item, spider):
        self.log.error(failure)

