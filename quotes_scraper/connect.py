import os
from mongoengine import connect
from dotenv import load_dotenv

def connect_to_mongoDB():
    """
    Підключається до бази даних MongoDB.
    """
    load_dotenv() # відкариває файл .env і завантажує змінні середовища

    # отримує URI підключення до MongoDB з змінної середовища
    MONGODB_URI = os.getenv("MONGODB_URI")

    # підключається до серверу MongoDB Atlass і використовує базу даних "quotes_db"
    connect(db="quotes_db", host=MONGODB_URI)