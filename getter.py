from abc import abstractclassmethod,ABC

# Изначально планировалось использовать паттерн стратегия, для замены алгоритма поиска цены актива в рилтайм
class Getter(ABC):
    @abstractclassmethod
    def getPrice(param:str):
        pass
    