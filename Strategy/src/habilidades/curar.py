from .interface import IHabilidade

class Curar(IHabilidade):

    def __init__(self, nivel):
        self.nivel = nivel

    def comportamento(self):
        print("Curar personagem.")

    def nivel_atributo(self):
        print("Nivel de cura: {} ".format(self.nivel))