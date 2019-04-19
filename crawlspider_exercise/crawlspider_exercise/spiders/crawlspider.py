# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class CrawlspiderSpider(CrawlSpider):
    name = 'crawlspider'
    start_urls = ['http://tieba.baidu.com/f?fr=wwwt&kw=%E6%96%B0%E5%9E%A3%E7%BB%93%E8%A1%A3']

    rules = (Rule(LinkExtractor(allow_domains=['baidu.com'], restrict_xpaths="*//a[@class='j_th_tit ']"), callback='parse_item'),)

    def parse_item(self, response):
        print(response.status)
