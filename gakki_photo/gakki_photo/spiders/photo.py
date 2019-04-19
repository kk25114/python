# -*- coding: utf-8 -*-
import scrapy
from gakki_photo.items import GakkiPhotoItem



class PhotoSpider(scrapy.Spider):
    name = 'photo'
    start_urls = ['https://movie.douban.com/celebrity/1018562/photos/?start={}'.format(str(i*30))for i in range(30)]


    def parse(self, response):
        href_list = response.xpath("//div[@class='cover']/a/@href").extract()
        for href in href_list:
            yield scrapy.Request(url=href, callback=self.parse_photo)

    def parse_photo(self, response):
        photo = response.xpath("//a[@class='mainphoto']/img/@src").extract()
        item = GakkiPhotoItem()
        item['image_urls'] = photo
        yield item