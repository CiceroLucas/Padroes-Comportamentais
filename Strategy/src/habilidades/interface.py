from abc import ABC, abstractclassmethod

class IHabilidade(ABC):

    @abstractclassmethod
    def comportamento(self):
        pass

    @abstractclassmethod
    def nivel_atributo(self):
        pass