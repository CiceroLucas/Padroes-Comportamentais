from abc import ABC, abstractclassmethod

class IEstado(ABC):

    @abstractclassmethod
    def esquentar(self):
        pass

    @abstractclassmethod
    def esfriar(self):
        pass

    def __repr__(self):
        return self.__class__.__name__