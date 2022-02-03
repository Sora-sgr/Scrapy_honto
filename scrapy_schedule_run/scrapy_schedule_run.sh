#!/bin/sh

echo "Hello, World!"

cd /Users/taiga/Programiming/Scrapy_Study/scrapy_honto
scrapy crawl scrapy_test_spider -o cron_test.json

# curl http://localhost:6800/schedule.json -d project=default -d spider=scrapy_test_spider



