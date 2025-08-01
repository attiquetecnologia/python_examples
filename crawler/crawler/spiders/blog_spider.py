import scrapy

class BlogSpider(scrapy.Spider):
    name = 'blog'  # Nome único do seu spider
    start_urls = ['https://www.tecmundo.com.br/tags/apps'] # URL(s) por onde o spider começará a rastrear

    def parse(self, response):
        # Este método é chamado para cada URL em start_urls
        # e para cada URL que o spider seguir a partir daqui.

        # Extrair títulos de posts
        # Usamos seletores CSS. O 'h2.entry-title a::text' seleciona o texto
        # dentro de tags <a> que estão dentro de <h2> com a classe 'entry-title'.
        titles = response.css('article.relative a::text').getall()
        for title in titles:
            yield {
                'title': title.strip() # Remove espaços em branco extras
            }

        # Seguir para a próxima página (se houver)
        # O 'a.next-posts-link::attr(href)' seleciona o valor do atributo 'href'
        # da tag <a> com a classe 'next-posts-link'.
        next_page = response.css('a.next-posts-link::attr(href)').get()
        if next_page is not None:
            # Se encontrar um link para a próxima página, faz uma nova requisição
            # e chama o método 'parse' novamente para processar a nova página.
            yield response.follow(next_page, callback=self.parse)