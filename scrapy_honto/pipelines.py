# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from tkinter import commondialog
from itemadapter import ItemAdapter
import pymysql
import os
import datetime


class ScrapyHontoPipeline:
    conn = None
    
    @classmethod
    def get_database(cls):
        
        cls.conn = pymysql.connect(
            host = "localhost",
            user = "root",
            # password = "",
            db = "hontodb",
            charset = "utf8",
            cursorclass=pymysql.cursors.DictCursor,
        )
        
        # テーブルを新規作成
        with cls.conn.cursor() as cursor:
            sql = "CREATE TABLE IF NOT EXISTS books(\
                id int not null primary key auto_increment, \
                book_title varchar(255) not null \
            ); "
            cursor.execute(sql)
            cls.conn.commit()        
                               
        return cls.conn
        
    def process_item(self, item, spider):
        '''
        Pipeline にデータが渡される時に実行される
        item に spider から渡された item がセットされる
        '''
        self.save_item(item)
        return item
        
    def save_item(self, item):
        # itemをDBに保存
        if self.find_same_db(item["book_title"]):
            # 既に同じURLのデータが存在する場合はスキップ
            print("スキップ")
            return
        
        conn = self.get_database()
        
        print("これからitem[\"book_title\"]を出力するよ")
        print(len(item["book_title"]))
        print(item["book_title"])
        
        with conn.cursor() as cursor:
            print("これからsave_itemのSQL実行するよ")
            sql = "INSERT INTO books (id, book_title) VALUES (%s, %s)"
            cursor.execute(sql, (0, item["book_title"]))
            conn.commit()
            
    def find_same_db(self, book_title):
        # すでに同じURLのDBがあれば取得
        conn = self.get_database()
        with conn.cursor() as cursor:
            print("find_same_dbのSQLを実行するよ")
            sql = "SELECT * FROM books WHERE book_title=%s"
            cursor.execute(sql, book_title)
            
        res = cursor.fetchone()
        print("resを表示するよ")  # {'id': 1479, 'book_title': '呪術廻戦 18'}
        print(res)
        return res
