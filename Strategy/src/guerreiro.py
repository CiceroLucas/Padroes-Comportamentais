from typing import Type
from .habilidades import IHabilidade

class Guerreiro:

    def __init__(self, habilidade: Type[IHabilidade]):
        self.habilidade = habilidade

    def acao(self):
        self.habilidade.comportamento()

    def nivel(self):
        self.habilidade.nivel_atributo()

        