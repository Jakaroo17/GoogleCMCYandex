# GoogleCMCYandex
Я по совместительству являюсь криптоинвестером и инвестором в акции в целом.У меня была проблема в том что учет своих инвестиций я вел в гугл таблицах. 
Заполнение цены по каждой акции занимало достаточно много времени и часто сталкивался c тем что цена за уже заполненные акции была неактуальной.
Я решил это дело как-то более менее автоматизировать. 

Эти скрипты заточены конкретно под мои нужды и не предназначены для кого-то конкретного. Однако если кому надо, то кто угодно может взять\модифицировать и прочее


О структуре:
Все состоит из 4 классов. 2 класса парсера (getcmcdata.py,getyandexdata.py), которые будут отвечать за получения цены с CoinMarketCap и Yandex.Инвестиций, 
класс для записи все в гугл докс (googledocks.py)
и класс посредник, который бы совмещал все воедино (middleman.py) 
Сначала планировалось использовать паттерн стратегия, для замены алгоритмов поиска цен в рил тайм, но изначальная цель была создать рабочий прототип.

Изначально планировалось использовать API coinmarketcap и яндекс.инвестиции, но так как у яндекса отсутсвует свое апи, а у CMC необходимо платить за подписку, было решено парсить цену

Все будет модифицироваться и изменяться в скором времени, ибо время выполнения приложения - 35 секунд, что удовлетворительно, но можно лучше
