from getter import Getter
import requests
from bs4 import BeautifulSoup

# Класс-парсер с единственным методом получения цены по криптовалюте с биржи CoinmarketCap
class CMC(Getter):
    # Метод получает название криптовалюты и переходит на страницу с ней в CoinMarketCap
    def getPrice(self,param: str):
        try:
            # Ссыль с нужной криптовалютой
            url = f'https://coinmarketcap.com/currencies/{param}'
            page = requests.get(url)

            soup = BeautifulSoup(page.text,'html.parser')
            # Поиск нужного тега из html
            price = soup.find(class_ = 'priceValue').text
            # Цена за монету получается сырой и непригодной для подсчета ($45,124.41). 4 реплайса позволит получить 
            # нормальную цифру для подстановки в Гугл докс (45124,41)
            price = price.replace('$','')
            price = price.replace('<','')
            price = price.replace(',','')
            price = price.replace('.',',')
            return price
        except Exception:
            print(Exception)
            



