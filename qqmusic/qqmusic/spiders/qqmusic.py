# -*- coding: utf-8 -*-
import scrapy
import json
import os
from qqmusic.items import QqmusicItem
headers = {
        "referer": "https://y.qq.com /n/yqq/song/003POTRK2Potzg.html",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
    }
class QqmusicSpider(scrapy.Spider):
    name = 'qqmusic'
    headers = {
        "referer": "https://y.qq.com /n/yqq/song/003POTRK2Potzg.html",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
    }

    def start_requests(self):
        url = "https://c.y.qq.com/v8/fcg-bin/fcg_v8_album_info_cp.fcg?albummid=0033XK9x1tBpf3&g_tk=5381&jsonpCallback=getAlbumInfoCallback&loginUin=0&hostUin=0&format=jsonp&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0"
        yield scrapy.Request(url=url, callback=self.parse, headers=headers)

    def parse(self, response):
        album_info = json.loads(response.text.split("getAlbumInfoCallback(")[-1].strip(")"))

        url = "https://c.y.qq.com/base/fcgi-bin/fcg_music_express_mobile3.fcg?g_tk=5381&jsonpCallback=MusicJsonCallback16951604912596197&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0&cid=205361747&callback=MusicJsonCallback16951604912596197&uin=0&songmid={songid}&filename=C400{songid}.m4a&guid=1841289520"
        for melody in album_info["data"]["list"][0:1]:
            yield scrapy.Request(url=url.format(songid=melody["songmid"]), callback=self.parse_music, headers=headers, meta={"name":melody["songname"]})

    def parse_music(self, response):
        headers = {
        "Accept": "* / *",
        "Accept - Encoding": "identity;q = 1, *;q = 0",
        "Accept - Language": "zh - CN, zh; q = 0.9",
        "Connection": "keep - alive",
        "Cookie": "pgv_pvi = 1433340928;RK = exKhTqMxV /;ptcz = ab563d7d80ab4b7c5065ff8eeec470b9ee981df4e86bdf08912de986bf6d0583;pt2gguin = o1300985820;tvfe_boss_uuid = 2ae5371d13125703;pgv_pvid = 1841289520;o_cookie = 1300985820;pgv_si = s9082845184;",
        "Host": "dl.stream.qqmusic.qq.com",
        "Range": "bytes = 0 -",
        "User - Agent": "Mozilla / 5.0(WindowsNT10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 65.0.3325.181Safari / 537.36"
        }

        download_param = json.loads(response.text.split("MusicJsonCallback16951604912596197(")[-1].strip(")"))
        mid = download_param["data"]["items"][0]["songmid"]
        vkey = download_param["data"]["items"][0]["vkey"]

        url = "http://dl.stream.qqmusic.qq.com/C400{mid}.m4a?vkey={vkey}&guid=18412".format(mid=mid, vkey=vkey)

        yield scrapy.Request(url=url, callback=self.savemusic, headers=self.headers)

    def savemusic(self, response):
        print(response.status)