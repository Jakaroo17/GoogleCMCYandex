from getcmcdata import CMC
from getyandexdata import Yandex
from googledocs import GoogleDocs


cmc_parser = CMC()
yandex_parser = Yandex()
google_sheet_wrr = GoogleDocs()

def getActives(*,letter:str,numstart:int,numend:int):
    end_symbol = google_sheet_wrr.find_by_column('Накопления',letter,numstart,numend,'END')
    digit = ''.join([a for a in end_symbol if a in '0123456789'])
    letter = ''.join([a for a in end_symbol if a not in digit])
    return google_sheet_wrr.get_data_from_sheets('Накопления',f'{letter}{numstart}',f'{letter}{int(digit)-1}','COLUMNS')['values'][0]

 #Список ликвидностей для поиска цены

cryptos = getActives(letter='K',numstart=23,numend=80)
stocks= getActives(letter='A',numstart=35,numend=80)
stocks_eu = getActives(letter='A',numstart=69,numend=90)
stocks_usd = getActives(letter='L',numstart=69,numend=90)
fonds   = getActives(letter='L',numstart=41,numend=80)
# bonds= getActives(letter='A',numstart=57,numend=90)




while True:
    # Заполнения списка ценами за крипту

    crypto_price=[]
    for x in cryptos:
        crypto_price.append(cmc_parser.getPrice(x))
    print(google_sheet_wrr.write_to_sheets('Накопления',f'P23',f'P{23+len(crypto_price)}',crypto_price,'COLUMNS'))
    print('-'*20,'Crypto - OK','-'*20)

    # Заполнения списка ценами за акции
    stock_ru_price = []
    for x in stocks:    
        stock_ru_price.append(yandex_parser.getPrice('stock',str.lower(x)))
    print(google_sheet_wrr.write_to_sheets('Накопления',f'G35',f'G{35+len(stock_ru_price)}',stock_ru_price,'COLUMNS'))
    print('-'*20,'RuStocks - OK','-'*20)
    # Заполнения списка ценами за евроакции
    stock_eu_price = []
    for x in stocks_eu:
        stock_eu_price.append(yandex_parser.getPrice('stock',str.lower(x)))
    print(google_sheet_wrr.write_to_sheets('Накопления',f'I{69}',f'I{69+len(stock_eu_price)}',stock_eu_price,'COLUMNS'))
    print('-'*20,'EuStocks - OK','-'*20)
    # Заполнения списка ценами за долларовые акции
    stock_usd_price = []
    for x in stocks_usd:
        stock_usd_price.append(yandex_parser.getPrice('stock',str.lower(x)))
    print(google_sheet_wrr.write_to_sheets('Накопления',f'S{69}',f'S{69+len(stock_usd_price)}',stock_usd_price,'COLUMNS'))
    print('-'*20,'UsdStocks - OK','-'*20)
    # Заполнения списка ценами за фонд
    fund_ru_price = []
    for x in fonds:
        fund_ru_price.append(yandex_parser.getPrice('fund',str.lower(x)))
    print(google_sheet_wrr.write_to_sheets('Накопления',f'R41',f'R{41   +len(fund_ru_price)}',fund_ru_price,'COLUMNS'))
    print('-'*20,'Funds - OK','-'*20)
    # Заполнения списка ценами за фонд в исс
    
    bond_ru_price = []
    for x in bonds:
        bond_ru_price.append(yandex_parser.getPrice('bond',str.lower(x)))
    print(google_sheet_wrr.write_to_sheets('Накопления',f'G57',f'G{57+len(bond_ru_price)}',bond_ru_price,'COLUMNS'))
    print('-'*20,'Bonds - OK','-'*20)
    # запись всего в гугл таблицы








