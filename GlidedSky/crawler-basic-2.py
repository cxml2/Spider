"""
@author: 寒菱
@software: PyCharm
@file: crawler-basic-2.py
@time: 2021-06-02 21:42
@email: 1782509343@qq.com
@desc: crawler-basic-2
"""

import feapder

from GlidedSky.config import USERNAME, PASSWORD


class FirstSpider(feapder.AirSpider):
    __custom_setting__ = dict(
        # 随机headers
        RANDOM_HEADERS=False,
        # requests 使用session
        USE_SESSION=True
    )

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
        yield feapder.Request("http://www.glidedsky.com/level/web/crawler-basic-2",
                              callback=self.parsePage,
                              number=0)

    def parsePage(self, req, resp):
        numbers = resp.xpath('//div[@class="col-md-1"]//text()').extract()
        numbers = sum(map(int, numbers))
        if req.number:
            numbers += req.number

        # 翻页
        href = resp.xpath('//a[@rel="next"]/@href').extract_first()
        if href:
            yield feapder.Request(href, callback=self.parsePage, number=numbers)
        else:
            print(numbers)


if __name__ == "__main__":
    FirstSpider().start()