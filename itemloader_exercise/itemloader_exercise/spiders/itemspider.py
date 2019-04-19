# -*- coding: utf-8 -*-
import scrapy
from itemloader_exercise.items import ItemloaderExerciseItem
from scrapy.loader import ItemLoader


class ItemspiderSpider(scrapy.Spider):
    name = 'itemspider'

    start_urls = ['http://tieba.baidu.com/f?fr=wwwt&kw=%E6%96%B0%E5%9E%A3%E7%BB%93%E8%A1%A3']

    def parse(self, response):
        i = ItemLoader(item=ItemloaderExerciseItem(), response=response)
        i.add_xpath('name', "//a[@class='j_th_tit ']//@title")
        i.add_xpath('url', "//a[@class='j_th_tit ']//@href")
        return i.load_item()

