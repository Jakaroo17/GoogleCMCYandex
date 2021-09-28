from abc import abstractclassmethod,ABC

# Изначально планировалось использовать паттерн стратегия, для замены алгоритма поиска цены активов в рилтайм
class Getter(ABC):
    @abstractclassmethod
    def getPrice(param:str):
        pass
    