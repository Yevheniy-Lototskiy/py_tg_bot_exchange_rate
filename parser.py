import requests
from bs4 import BeautifulSoup

EXCHANGE_RATE_URL = "https://www.google.com/finance/quote/USD-UAH"


def get_exchange_rate() -> float:
    exchange_rate_page = requests.get(EXCHANGE_RATE_URL).content
    soup = BeautifulSoup(exchange_rate_page, "html.parser")

    exchange_rate = float(soup.find("div", {"data-entity-type": "3"}).get("data-last-price"))
    rounded_exchange_rate = round(exchange_rate, 4)

    return rounded_exchange_rate
