# config.py
import os


class Config:
    BASE_URL = "http://5.101.50.27:8000"
    AUTH_USERNAME = "harrypotter"
    AUTH_PASSWORD = "expelliarmus"

    # Таймауты
    DEFAULT_TIMEOUT = 10

    # Заголовки
    HEADERS = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }