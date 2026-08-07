import json

from scraper.items import QuoteItem, AuthorItem


class JsonWriterPipeline:
    def __init__(self):
        self.quotes = []
        self.authors = []

    def process_item(self, item, spider):
        if isinstance(item, QuoteItem):
            self.quotes.append(dict(item))

        elif isinstance(item, AuthorItem):
            self.authors.append(dict(item))

        return item

    def close_spider(self, spider):
        with open("quotes.json", "w", encoding="utf-8") as file:
            json.dump(self.quotes, file, ensure_ascii=False, indent=4)

        with open("authors.json", "w", encoding="utf-8") as file:
            json.dump(self.authors, file, ensure_ascii=False, indent=4)