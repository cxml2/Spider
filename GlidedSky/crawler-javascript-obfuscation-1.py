"""
@author: 寒菱
@software: PyCharm
@file: crawler-javascript-obfuscation-1.py
@time: 2021-06-02 23:33
@email: 1782509343@qq.com
@desc: crawler-javascript-obfuscation-1
"""
import hashlib
import math
import time

import feapder
from feapder.utils.tools import get_param

from GlidedSky.config import USERNAME, PASSWORD


class FirstSpider(feapder.AirSpider):
    __custom_setting__ = dict(
        # 随机headers
        RANDOM_HEADERS=False,
        # requests 使用session
        USE_SESSION=True
    )

    number = 0
    def start_requests(self):
        yield feapder.Request("http://www.glidedsky.com/login", callback=self.login)

    def login(self, request, response):
        token = response.xpath('//input[@name="_token"]/@value').extract_first()
        csrf = response.xpath('//meta[@name="csrf-token"]/@content').extract_first()
        yield feapder.Request("http://www.glidedsky.com/login",
                              data={
                                  '_token': token,
                                  'email': USERNAME,
                                  'password': PASSWORD
                              },
                              callback=self.parse
                              )

    def parse(self, req, resp):
        yield feapder.Request(f"http://www.glidedsky.com/level/web/crawler-javascript-obfuscation-1",
                              callback=self.parsePage)


    def parsePage(self, req, resp):
        p = resp.xpath('//div[@class="container"]/@p').extract_first()
        ts = resp.xpath('//div[@class="container"]/@t').extract_first()
        ts = math.floor((int(ts)-99) // 99)
        sign = hashlib.sha1(f'Xr0Z-javascript-obfuscation-1{ts}'.encode()).hexdigest()
        yield feapder.Request(f"http://www.glidedsky.com/api/level/web/crawler-javascript-obfuscation-1/items?page={p}&t={ts}&sign={sign}",
                              callback=self.parseItem,
                              )


    def parseItem(self, req, resp):
        items = resp.json['items']
        if items:
            self.number += sum(items)
            p = int(get_param(req.url, 'page')) + 1
            yield feapder.Request(f"http://www.glidedsky.com/level/web/crawler-javascript-obfuscation-1?page={p}",
                                  callback=self.parsePage)
        else:
            print(self.number)


'''
let p = $('main .container').attr('p');
let t = Math.floor( / 99);
let sign = sha1('Xr0Z-javascript-obfuscation-1' + t);
$.get('/api/level/web/crawler-javascript-obfuscation-1/items?page=' + p + '&t=' + t + '&sign=' + sign, function (data) {
    const list = JSON.parse(data).items;
    $('.col-md-1').each(function (index) {
        if (list && index < list.length) {
            $('.col-md-1').eq(index).text(list[index])
        }
    })
})
'''


if __name__ == "__main__":
    FirstSpider().start()
