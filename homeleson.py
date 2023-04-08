import requests
from bs4 import BeautifulSoup
class CurrencyConverter:
    def __init__(self):
        self.rates = {}
    response = requests.get("https://coinmarketcap.com/")
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, features="html.parser")
        soup_list = soup.find_all("a", {"href": "/currencies/bitcoin/markets/"})
        res = soup_list[0].find("span")
        print(res.text)

RubToDollar = 0.012136
cash = int(input('Введите количество денег: '))
currency = input('В какой валюте введены деньги (руб, доллар)? ')
match currency:
   case "руб":
       print(f'{cash} руб в долларах: {int(cash * RubToDollar)}')
   case "доллар":
       print(f'{cash} доллар(-ов) в рублях: {int(cash / RubToDollar)}')