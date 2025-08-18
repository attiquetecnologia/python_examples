from pathlib import Path

import scrapy


class QuotesSpider(scrapy.Spider):
    name = "postagens"

    async def start(self):
        urls = [
            "http://127.0.0.1:8000",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for l in response.css(".card"):
            yield {
                'titulo': l.css(".card-title::text").get()
            }