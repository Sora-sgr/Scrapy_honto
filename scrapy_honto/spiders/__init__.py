# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

from datetime import datetime
from pprint import pprint
from xmlrpc.client import NOT_WELLFORMED_ERROR
import scrapy
from scrapy_honto.items import ScrapyHontoItem

class ScrapyTestSpider(scrapy.Spider):
    name = 'scrapy_test_spider'
    # allowed_domains = ['pasonatech.co.jp']
    allowed_domains = ['honto.jp']
    # start_urls = ['https://www.pasonatech.co.jp/']
    # start_urls = ['https://honto.jp/ranking/gr/bestseller_1101_1201_011_029004000000.html', 'https://honto.jp/ranking/gr/bestseller_1101_1204_012_029004000000.html']
    start_urls = ['https://honto.jp/ranking/gr/bestseller_1101_1201_011_029004000000.html']

    def parse(self, response):
        #  return ScrapyHontoItem(
        #         title = response.css('title').extract_first().strip(),
        #     )
        
        # response.css で scrapy デフォルトの css セレクタを利用できる
        book_titles = response.css("h2.stHeading a::text").extract()
        
        print()
        print("book_titleをこれから出力するよ")
        pprint(book_titles)
        print()
        
        dt = datetime.now()
        print("datetime.now()の結果", dt)
        
        # # response.css で scrapy デフォルトの css セレクタを利用できる
        # for book in response.css("div.stBoxLine01"):
        #     # items に定義した ScrapyHontoItem のオブジェクトを生成して次の処理へ渡す
        #     yield ScrapyHontoItem(
        #         book_title=book.css("h2.stHeading a::text"),
        #         rank_num=int(book.css("p.stNum em::text")),
        #         date_time=str(dt),
        #         url=starts_url[]
        #     )

        
        # response.css で scrapy デフォルトの css セレクタを利用できる
        for book in response.css("h2.stHeading a::text").extract():
            # items に定義した ScrapyHontoItem のオブジェクトを生成して次の処理へ渡す
            yield ScrapyHontoItem(
                book_title=book
            )
            
        # for book in response.css("p.stNum"):
        #     yield ScrapyHontoItem(
        #         book_rank_num=book.e
        #         book_title=book.extract_first().strip(),
        #     )
