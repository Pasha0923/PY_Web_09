import scrapy
from scraper.items import QuoteItem , AuthorItem

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]

    visited_authors = set()

    def parse(self, response):
        quotes = response.css("div.quote")

        self.logger.info(f"Found quotes: {len(quotes)}")

        for quote in quotes:
            item = QuoteItem()

            item["quote"] = quote.css("span.text::text").get()
            item["author"] = quote.css("small.author::text").get()
            item["tags"] = quote.css("a.tag::text").getall()

            yield item
        # Отримуємо URL автора та перевіряємо, чи ми вже відвідали його сторінку
            author_url = quote.css("small.author ~ a::attr(href)").get()
        # Якщо ми ще не відвідали сторінку автора, додаємо її до списку відвіданих та викликаємо метод parse_author
            if author_url not in self.visited_authors:
                self.visited_authors.add(author_url)
                yield response.follow(author_url, callback=self.parse_author)

        next_page = response.css("li.next a::attr(href)").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)


    def parse_author(self, response):
        self.logger.info(f"Author page: {response.url}")
        item = AuthorItem()

        item["fullname"] = response.css("h3.author-title::text").get().strip()
        item["born_date"] = response.css(".author-born-date::text").get()
        item["born_location"] = response.css(".author-born-location::text").get()
        item["description"] = response.css(".author-description::text").get().strip()

        yield item