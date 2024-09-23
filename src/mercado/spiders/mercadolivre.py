import scrapy


class MercadolivreSpider(scrapy.Spider):
    name = "mercadolivre"
    allowed_domains = ["lista.mercadolivre.com.br"]
    start_urls = ["https://lista.mercadolivre.com.br/tenis-corrida-masculino"]
    page_count = 1
    max_pages = 4

    def parse(self, response):
        products = response.css('div.poly-card__content')
        
        for product in products:
            yield {
                'brand': product.css('span.poly-component__brand::text').get(),
                'name': product.css('h2.poly-box.poly-component__title::text').get(),
                'new_price': product.css('div.poly-price__current::text').get()
                   }
            
        if self.page_count < self.max_pages:
            next_page = response.css('li.andes-pagination__button.andes-pagination__button--next::attr(href)').get()
            if next_page:
                self.page_count += 1
                yield scrapy.Request(url=next_page, callback=self.parse)
