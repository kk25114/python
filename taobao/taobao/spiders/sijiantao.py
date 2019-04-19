# -*- coding: utf-8 -*-
import scrapy
from taobao.items import TaobaoItem
from scrapy.http import Request


cookies = {
    'hng':'CN%7Czh-CN%7CCNY%7C156',
    ' cna':'CSA1EwYU8QQCAXjsroUMn1Za',
    ' _med':'dw:1536&dh:864&pw:1920&ph:1080&ist:0',
    ' tk_trace':'1',' t':'6e0e59840674a669f218cc3dafd5d170',
    ' _tb_token_':'f4365ded8316',
    ' cookie2':'118134bb8eee5ed9901a89ce54937129',
    ' _m_h5_tk':'51731ba16fbb6cab4af6958fcecd8cf9_1525015570850',
    ' _m_h5_tk_enc':'c204893d32b98223cf547ead3902cb72',
    ' dnk':'%5Cu666E%5Cu901A%5Cu559C%5Cu8863%5Cu7C89',
    ' uc1':'cookie14=UoTeO82gnE3reg%3D%3D&lng=zh_CN&cookie16=URm48syIJ1yk0MX2J7mAAEhTuw%3D%3D&existShop=alse&cookie21=UtASsssmeW6lpyd%2BB%2B3t&tag=8&cookie15=Vq8l%2BKCLz3%2F65A%3D%3D&pas=0',
    ' uc3':'nk2=pZfQ1pXpFLYOjQ%3D%3D&id2=UU8M%2B7F5BLQoVg%3D%3D&vt3=F8dBz4FW27yAVCQuSC8%3D&lg2=V32FPkk%2Fw0dUvg%3D%3D',
    ' tracknick':'%5Cu666E%5Cu901A%5Cu559C%5Cu8863%5Cu7C89',
    ' lid':'%E6%99%AE%E9%80%9A%E5%96%9C%E8%A1%A3%E7%B2%89',
    ' _l_g_':'Ug%3D%3D',
    ' unb':'2749646276',
    ' lgc':'%5Cu666E%5Cu901A%5Cu559C%5Cu8863%5Cu7C89',
    ' cookie1':'BxFkIVOFtcaUHRJ8z7dHOapfk1wT6ZzOhhCXX89goXI%3D',
    ' login':'true',
    ' cookie17':'UU8M%2B7F5BLQoVg%3D%3D',
    ' _nk_':'%5Cu666E%5Cu901A%5Cu559C%5Cu8863%5Cu7C89',
    ' sg':'%E7%B2%896a',
    ' csg':'37e195c7',
    ' cq':'ccp%3D0',
    ' enc':'hV8rAdGGx%2FHCs8G7tFTdikSKA1pweV5MlZ29aQTUUPP1b0XW7pdV4mfpP7Lt8JtbwRYEmtk7sAhp%2FL1bwm%2Bgzg%3D%3D',' tt':'tmall-main',' otherx':'e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0',' swfstore':'195833',' res':'scroll%3A1519*5566-client%3A1519*734-offset%3A1519*5566-screen%3A1536*864',' pnm_cku822':'098%23E1hvUQvUvbpvUpCkvvvvvjiPPF5v1j3CP2cyAjljPmPv0jDPn2qUsjDEn2SWQj3PPuwCvvpvvUmmRphvCvvvvvvCvpvVvvpvvhCvmphvLvpYCvvjOezUaNpqrADn9WmQD40Xjo2v%2B8c6eC3tpnoQ0f06WeCpqU0HsfUpwZNIAXcBKFyK2ixrAj7JVVQHYnsp0EQ7nDeDyO2v5fVEvpvVmvvC9jX2uphvmvvv9bHBKh44Kphv8vvvvvCvpvvvvvv2vhCvmj%2BvvvWvphvW9pvvvQCvpvs9vvv2vhCv2RvPvpvhvvvvvv%3D%3D',' whl':'-1%260%260%260',' x':'__ll%3D-1%26_ato%3D0',' isg':'BBISw7rRnEiniOA1qfTU6BL7Y9g0ixbXB_IsGtxru0W977LpxLNmzRhOW0tTmY5V'
}

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
}



class SijiantaoSpider(scrapy.Spider):
    name = 'sijiantao'

    start_urls = ['https://list.tmall.com/search_product.htm?s={}&q=%CB%C4%BC%FE%CC%D7'.format(str(i*60)) for i in range(30)]

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url=url, cookies=cookies, headers=headers)

    def parse(self, response):
        prices = response.xpath("//p[@class='productPrice']/em/text()").extract()
        sale_volumes = response.xpath("//p[@class='productStatus']//em/text()").extract()
        titles = response.xpath("//p[@class='productTitle']/a/@title").extract()
        comments = response.xpath("//p[@class='productStatus']/span[2]/a/text()").extract()
        shops = response.xpath("//a[@class='productShop-name']/text()").extract()
        for price, sale_volume, title, comment, shop in zip(prices, sale_volumes, titles, comments, shops):
            item = TaobaoItem()
            item['price'] = price
            item['sale_volume'] = sale_volume
            item['comment'] = comment
            item['title'] = title
            item['shop'] = shop
            yield item





