import scrapy

#https://medium.com/@marlessonsantana/utilizando-o-scrapy-do-python-para-monitoramento-em-sites-de-not%C3%ADcias-web-crawler-ebdf7f1e4966
class Sp1Spider(scrapy.Spider):
    name = "sp1"
    allowed_domains = ["casabellabarretos.com.br"]
    start_urls = ["https://casabellabarretos.com.br/"]

    def parse(self, response):
        
        for article in response.css("row"):
            print("Response", article)
            # link = article.css("div.texts h2 a::attr(href)").extract_first()
            # title = article.css("div.texts h2 a::attr(href)").extract_first()
            # author = article.css("div.texts div.infoa::text").extract_first()

        #     yield {'link': link, 'title': title, 'author': author}
