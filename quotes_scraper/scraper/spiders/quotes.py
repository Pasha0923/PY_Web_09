import scrapy
from scraper.items import QuoteItem

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]

    def parse(self, response):
        quotes = response.css("div.quote")
        self.logger.info(f"Found quotes: {len(quotes)}")

        for quote in quotes:
            item = QuoteItem()

            item["quote"] = quote.css("span.text::text").get()
            item["author"] = quote.css("small.author::text").get()
            item["tags"] = quote.css("a.tag::text").getall()

            yield item

        next_page = response.css("li.next a::attr(href)").get()

        if next_page:
            yield response.follow(next_page, callback=self.parse)