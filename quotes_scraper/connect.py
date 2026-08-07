from mongoengine import connect
from dotenv import load_dotenv
import os

# відкариває файл .env і завантажує змінні середовища

# load_dotenv()

# MONGODB_URI = os.getenv("MONGODB_URI")

# # підключається до бази даних MongoDB за допомогою URI з файлу .env
# connect(db="quotes_db", host=MONGODB_URI)

def connect_to_mongoDB():
    """
    Підключається до бази даних MongoDB.
    """
    load_dotenv()

    MONGODB_URI = os.getenv("MONGODB_URI")

    connect(db="quotes_db", host=MONGODB_URI)