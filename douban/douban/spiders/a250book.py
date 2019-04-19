# -*- coding: utf-8 -*-
import scrapy
from douban.items import DoubanItem
from scrapy.shell import inspect_response


class A250bookSpider(scrapy.Spider):
    name = '250book'
    start_urls = ['https://book.douban.com/top250?start={}'.format(str(i*25))for i in range(10)]

    def star_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        # inspect_response(response, self)
        titles = response.xpath('//div[@class="pl2"] /a/@title').extract()
        infos = response.xpath("//p[@class='pl']/text()").extract()
        scores = response.xpath("//span[@class='rating_nums']/text()").extract()
        xpaths = ["//div[@class='indent']/table[{}]//span[@class='inq']/text()".format(str(i)) for i in range(1, 26)]
        for title, info, score, xpath in zip(titles, infos, scores, xpaths):
            item = DoubanItem()
            item["book_name"] = title.encode("utf-8")
            item["author"] = info.split("/")[0]
            item["book_score"] = score.encode("utf-8")
            try:
                item["comment"] = response.xpath(xpath).extract()[0]
            except IndexError:
                item["comment"] = ""
            yield item

