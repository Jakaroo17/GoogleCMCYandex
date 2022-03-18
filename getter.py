from abc import abstractclassmethod,ABC

# Изначально планировалось использовать паттерн стратегия, для замены алгоритма поиска цены активов в рилтайм
# Had idea to use pattern Strategy for replacing algorythms of searching prices realtime 
class Getter(ABC):
    @abstractclassmethod
    def getPrice(param:str):
        pass
    