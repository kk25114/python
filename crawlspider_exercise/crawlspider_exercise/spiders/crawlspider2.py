# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from crawlspider_exercise.items import CrawlspiderExerciseItem

class Crawlspider2Spider(scrapy.Spider):
    name = 'crawlspider2'
    allowed_domains = ['baidu.com']
    start_urls = ['http://tieba.baidu.com/f?fr=wwwt&kw=%E6%96%B0%E5%9E%A3%E7%BB%93%E8%A1%A3']

    def parse(self, response):
        links = LinkExtractor(tags=('a', ), attrs=('href', )).extract_links(response)
        for lin in links:
            print(lin.text)
