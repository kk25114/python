# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import TutorialItem


class BookSpider(scrapy.Spider):
    name = 'book'
    start_urls = ['https://docs.scrapy.org/en/latest/']
    root_url = "https://docs.scrapy.org/en/latest/"

    def parse(self, response):
        urls = response.xpath("//a[@class='reference internal']/@href").extract()
        titles = response.xpath("//a[@class='reference internal']/text()").extract()

        for request, title in zip(urls, titles):
            yield scrapy.Request(self.root_url+request, callback=self.parse_content, meta={"title": title})
        # content = response.xpath("//div[@role='main']").extract()[0].encode("utf-8")
        # item = TutorialItem()
        # item['content'] = content
        # yield item
        # yield

    def parse_content(self, response):
        content = response.xpath("//div[@role='main']").extract()[0]
        item = TutorialItem()
        item["title"] = response.meta['title']
        item['content'] = content
        yield item


