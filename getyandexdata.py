
from getter import Getter
import requests
from bs4 import BeautifulSoup

# Класс парсера для яндекс акции с единственной функцией получения цены за акцию
class Yandex(Getter):
  def getPrice(self,types: str,param: str):
        try:
            url = f'https://invest.yandex.ru/catalog/{types}/{param}'
            page = requests.get(url)
            soup = BeautifulSoup(page.text,'html.parser')
            if types != 'bond':
              price = soup.find(class_ = '_2SLlm0Udigxy-pfSsLmJbC').text
            else:
              price = soup.find(class_ = '_2NhGI8HVO_OG2E2pWl10IY').text
              price = price.replace('\u202f','')
              price = price.replace('$','')
              price = price.replace('₽','')
            
            return price
        except Exception:
            print(Exception)


