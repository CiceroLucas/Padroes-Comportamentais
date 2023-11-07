from .interface import IHabilidade

class LutaEspada(IHabilidade):

    def __init__(self, nivel):
        self.nivel = nivel

    def comportamento(self):
        print("Lutar com espada.")

    def nivel_atributo(self):
        print("Nivel de espada: {} ".format(self.nivel))