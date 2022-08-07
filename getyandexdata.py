import requests
from bs4 import BeautifulSoup

# Класс парсера для яндекс акции с единственной функцией получения цены за акцию
# Class-parser with only function getting bonds price from yandex investing
class Yandex():
  def getPrice(self,types: str,param: str):
        try:
            url = f'https://invest.yandex.ru/catalog/{types}/{param}'
            page = requests.get(url)
            soup = BeautifulSoup(page.text,'html.parser')
            if types != 'bond':
              # Теги в верстке HTML которые отвечают за цену. _2SLlm0Udigxy-pfSsLmJbC - акции и фонды 
              # Tags that's are responsible for price. _2SLlm0Udigxy-pfSsLmJbC - stocks and funds
              price = soup.find(class_ = 'bolbtRDz491tDq6jfmHd').text
            else:
              # _2NhGI8HVO_OG2E2pWl10IY - только облигации
              # _2NhGI8HVO_OG2E2pWl10IY - bonds only 
              price = soup.find(class_ = 'bolbtRDz491tDq6jfmHd').text
              price = price.replace('\u202f','')
              price = price.replace('$','')
              price = price.replace('₽','')
            price = price.replace(' ','')
            print(f'{param} -',price)
            return price
        except Exception as e:
            print(f'{param} - ', e)



