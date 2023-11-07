from .interface import IHabilidade

class LutaArco(IHabilidade):

    def __init__(self, nivel):
        self.nivel = nivel

    def comportamento(self):
        print("Lutar com arco.")

    def nivel_atributo(self):
        print("Nivel de arco: {} ".format(self.nivel))