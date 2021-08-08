import scrapy
import unittest
import requests

class MySpider(scrapy.Spider):
    url = "http://172.18.58.238/photography"
    r = requests.get(url)
    print(r.text)
    print("Status code:")
    print("\t *", r.status_code)
    h = requests.head(url)
    print("Header:")
    print("**********")
    for x in h.headers:
        print("\t", ":", h.headers[x])
    print("**********")
    headers ={
        "User-Agent" : "Mobile"
    }
    url2="http://172.18.58.238/headers.php"
    rh = requests.get(url2, headers=headers)
    print(rh.text)

import scrapy
class NewSpider(scrapy.Spider):
    name = "new_spider"
    start_urls=["http://172.18.58.238/photography"]
    def parse(self, response):
        css_selector = "img"
        for x in response.css(css_selector):
            newsel="@src"
            yield{
                "Image Link":x.xpath(newsel).extract_first(),
            }

    name = "new_spider"
    start_urls=["http://172.18.58.238/photography"]
    def parse(self,response):
        xpath_selector="//img"
        for x in response.xpath(xpath_selector):
            newsel="@src"
            yield{
                "Image Link":x.xpath(newsel).extract_first(),
            }

            Page_selector='.next a ::attr(href)'
            next_page=response.css(Page_selector).extract_first()
            if next_page:
                yield scrapy.Request(
                    response.urljoin(next_page),
                    callback=self.parse
                )

    class Test_MySpider(unittest.TestCase):
        def test_spider(self):
            MySpider()
