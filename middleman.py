from getcmcdata import CMC
from getyandexdata import Yandex
from googledocs import GoogleDocs

testcmcfunc = CMC()
tesyandexfunc = Yandex()
testgoogledocs = GoogleDocs()

def getActives(*,letter:str,numstart:int,numend:int):
    end_symbol = testgoogledocs.find_by_column('Накопления',letter,numstart,numend,'END')
    digit = ''.join([a for a in end_symbol if a in '0123456789'])
    letter = ''.join([a for a in end_symbol if a not in digit])
    return testgoogledocs.get_data_from_sheets('Накопления',f'{letter}{numstart}',f'{letter}{int(digit)-1}','COLUMNS')['values'][0],int(digit)-1



#Список ликвидностей для поиска цены

cryptos = getActives(letter='K',numstart=23,numend=80)
stocks= getActives(letter='A',numstart=35,numend=80)
stocks_eu = getActives(letter='A',numstart=69,numend=80)
stocks_usd = getActives(letter='L',numstart=69,numend=90)
fonds,= getActives(letter='L',numstart=57,numend=80)
fonds_iss = getActives(letter='R',numstart=23,numend=90)
bonds= getActives(letter='A',numstart=57,numend=90)





# Заполнения списка ценами за крипту
# crypto_price=[]
# for x in cryptos:
#     crypto_price.append(testcmcfunc.getPrice(x))
# print(testgoogledocs.write_to_sheets('Накопления',f'P23',f'P{23+len(crypto_price)}',crypto_price,'COLUMNS'))

# # Заполнения списка ценами за акции
# stock_ru_price = []
# for x in stocks:
#     stock_ru_price.append(tesyandexfunc.getPrice('stock',str.lower(x)))
# print(testgoogledocs.write_to_sheets('Накопления',f'G35',f'G{35+len(stock_ru_price)}',stock_ru_price,'COLUMNS'))

# # Заполнения списка ценами за евроакции
# stock_eu_price = []
# for x in stocks_eu:
#     stock_eu_price.append(tesyandexfunc.getPrice('stock',str.lower(x)))
# print(testgoogledocs.write_to_sheets('Накопления',f'I{42}',f'I{42+len(stock_eu_price)}',stock_eu_price,'COLUMNS'))
# # Заполнения списка ценами за долларовые акции
# stock_usd_price = []
# for x in stocks_usd:
#     stock_usd_price.append(tesyandexfunc.getPrice('stock',str.lower(x)))
# print(testgoogledocs.write_to_sheets('Накопления',f'H{43}',f'H{43+len(stock_usd_price)}',stock_usd_price,'COLUMNS'))
# # Заполнения списка ценами за фонд
# fund_ru_price = []
# for x in fonds:
#     fund_ru_price.append(tesyandexfunc.getPrice('fund',str.lower(x)))
# print(testgoogledocs.write_to_sheets('Накопления',f'G52',f'G{52+len(fund_ru_price)}',fund_ru_price,'COLUMNS'))
# # Заполнения списка ценами за фонд в исс
# fund_iss_price = []
# for x in fonds_iss:
#     fund_iss_price.append(tesyandexfunc.getPrice('fund',str.lower(x)))
# print(testgoogledocs.write_to_sheets('Накопления',f'X23',f'X{23+len(fund_iss_price)}',fund_iss_price,'COLUMNS'))
# # Заполнения списка ценами за облигации
# bond_ru_price = []
# for x in bonds:
#     bond_ru_price.append(tesyandexfunc.getPrice('bond',str.lower(x)))
# print(testgoogledocs.write_to_sheets('Накопления',f'G57',f'G{57+len(bond_ru_price)}',bond_ru_price,'COLUMNS'))
# # запись всего в гугл таблицы








