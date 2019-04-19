# -*- coding: utf-8 -*-
import scrapy


class GakkiDataInfoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    rank = scrapy.Field()
    exp = scrapy.Field()
    level = scrapy.Field()


class WwwBaiduComSpider(scrapy.Spider):
    name = 'gakki_info'
    start_urls = \
        ['http://tieba.baidu.com/f/like/furank?kw=%D0%C2%D4%AB%BD%E1%D2%C2&pn={}'.format(str(i)) for i in range(3746, 6692)]

    def parse(self, response):

        names = response.xpath("//tr[@class='drl_list_item']/td[2]//text()").extract()
        ranks = response.xpath("//tr[@class='drl_list_item']/td[1]//text()").extract()
        levels = response.xpath("//tr[@class='drl_list_item']/td[3]/div/@class").extract()
        exps = response.xpath("//tr[@class='drl_list_item']/td[4]//text()").extract()
        for name, rank, level, exp in zip(names, ranks, levels, exps):
            item = GakkiDataInfoItem()
            item['name'] = name
            item['rank'] = rank
            item['level'] = level
            item['exp'] = exp
            yield item
