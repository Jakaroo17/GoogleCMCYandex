import requests
from bs4 import BeautifulSoup

# Класс-парсер с единственным методом получения цены по криптовалюте с биржи CoinmarketCap
# Class-Parser with only method that gets cryptos price from CoinmarketCap
class CMC():
    # Метод получает название криптовалюты и переходит на страницу с ней в CoinMarketCap
    # Method that accepts cryptoname and opens website with its price
    def getPrice(self,param: str):
        try:
            # Ссыль с нужной криптовалютой
            # Link with some crypto
            url = f'https://coinmarketcap.com/currencies/{param}'
            page = requests.get(url)

            soup = BeautifulSoup(page.text,'html.parser')
            # Поиск нужного тега из html
            # Serching html tag with price
            price = soup.find(class_ = 'priceValue').text
            # Цена за монету получается сырой и непригодной для подсчета ($45,124.41). 4 реплейса позволит получить 
            # нормальную цифру для расчетов в Гугл докс (45124,41)
            # Price per coin is raw ($45,124.41). 4 replaces make it normal for inputing into Google Sheets (45124,41)
            price = price.replace('$','')
            price = price.replace('<','')
            price = price.replace(',','')
            price = price.replace('.',',')
            print(f'{param} - ',price)
            return price
        except Exception as e :
            print(f'{param} - ', e)
            



