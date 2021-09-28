from getcmcdata import CMC
from getyandexdata import Yandex
from googledocs import GoogleDocs

#Список ликвидностей для поиска цены 
сryptos = ['dogecoin','ethereum','bittorrent','bitcoin','binance-coin','bearhunt','tokocrypto','moonbear-finance','bumoon','redshiba','dent']
stocks = ['VTBR','KZOSP','LNTA','MRKC','MSST','RGSS','RUGR']
stocks_eu = ['DBK@DE']
stocks_usd = ['ENDP','F','GSKY','LPL','MFGP','WTTR','RIG','VEON','ZYNE']
fonds = ['VTBM','FXGD','FXIM','FXWO','FXRW'] 
fonds_iss = ['FXDM','FXES','FXDE','FXFA','FXIP','VTBM']
bonds = ['RU000A0JTMK9']

# Создание объктов парсеров и объекта записи в таблицы
testcmcfunc = CMC()
tesyandexfunc = Yandex()
testgoogledocs = GoogleDocs()

# Заполнения массива ценами за крипту
crypto_price=[]
for x in сryptos:
    crypto_price.append(testcmcfunc.getPrice(x))

# Заполнения массива ценами за акции
stock_ru_price = []
for x in stocks:
    stock_ru_price.append(tesyandexfunc.getPrice('stock',str.lower(x)))

# Заполнения массива ценами за евроакции
stock_eu_price = []
for x in stocks_eu:
    stock_eu_price.append(tesyandexfunc.getPrice('stock',str.lower(x)))

# Заполнения массива ценами за долларовые акции
stock_usd_price = []
for x in stocks_usd:
    stock_usd_price.append(tesyandexfunc.getPrice('stock',str.lower(x)))

# Заполнения массива ценами за фонд
fund_ru_price = []
for x in fonds:
    fund_ru_price.append(tesyandexfunc.getPrice('fund',str.lower(x)))

# Заполнения массива ценами за фонд в исс
fund_iss_price = []
for x in fonds_iss:
    fund_iss_price.append(tesyandexfunc.getPrice('fund',str.lower(x)))

# Заполнения массива ценами за облигации
bond_ru_price = []
for x in bonds:
    bond_ru_price.append(tesyandexfunc.getPrice('bond',str.lower(x)))

# запись всего в гугл таблицы
print(testgoogledocs.write_to_sheets('Накопления',f'P23',f'P{23+len(crypto_price)}',crypto_price,'COLUMNS'))
print(testgoogledocs.write_to_sheets('Накопления',f'G35',f'G{35+len(stock_ru_price)}',stock_ru_price,'COLUMNS'))
print(testgoogledocs.write_to_sheets('Накопления',f'I{42}',f'I{42+len(stock_eu_price)}',stock_eu_price,'COLUMNS'))
print(testgoogledocs.write_to_sheets('Накопления',f'H{43}',f'I{43+len(stock_usd_price)}',stock_usd_price,'COLUMNS'))
print(testgoogledocs.write_to_sheets('Накопления',f'G52',f'G{52+len(fund_ru_price)}',fund_ru_price,'COLUMNS'))
print(testgoogledocs.write_to_sheets('Накопления',f'X23',f'X{23+len(fund_iss_price)}',fund_iss_price,'COLUMNS'))
print(testgoogledocs.write_to_sheets('Накопления',f'G57',f'G{57+len(bond_ru_price)}',bond_ru_price,'COLUMNS'))


