import json
from connect import connect_to_mongoDB
from models import Author, Quote

def load_authors():
    with open("authors.json", "r", encoding="utf-8") as file:
        authors = json.load(file)

    for author in authors:
        Author(
            fullname=author["fullname"],
            born_date=author["born_date"],
            born_location=author["born_location"],
            description=author["description"],
        ).save()


def load_quotes():
    with open("quotes.json", "r", encoding="utf-8") as file:
        quotes = json.load(file)

    for quote in quotes:
        author = Author.objects(fullname=quote["author"]).first()

        Quote(
            tags=quote["tags"],
            author=author,
            quote=quote["quote"],
        ).save()


def main():
    connect_to_mongoDB()

    Author.drop_collection()
    Quote.drop_collection()

    load_authors()
    load_quotes()


if __name__ == "__main__":
    main()