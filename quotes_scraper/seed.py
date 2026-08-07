import json

from connect import *
from models import Author , Quote

connect_to_mongoDB()

# Удаляем старую коллекцию (если она существует)
Author.drop_collection()
Quote.drop_collection()

with open("authors.json", "r", encoding="utf-8") as file:
    authors = json.load(file)

# Добавляем каждого автора в MongoDB
for author in authors:
    new_author = Author(
        fullname=author["fullname"],
        born_date=author["born_date"],
        born_location=author["born_location"],
        description=author["description"],
    )

    new_author.save()

# ---------- Загрузка цитат ----------
with open("quotes.json", "r", encoding="utf-8") as file:
    quotes = json.load(file)

for quote in quotes:

    author = Author.objects(fullname=quote["author"]).first()

    new_quote = Quote(
        tags=quote["tags"],
        author=author,
        quote=quote["quote"],
    )
    new_quote.save()

print("Authors and quotes successfully loaded!")