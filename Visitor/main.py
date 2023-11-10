from abc import ABC, abstractmethod


class Parte(ABC):

    def __init__(self, numero, descricao):
        self.numero = numero
        self.descricao = descricao

    @abstractmethod
    def aceitar(self, visitante):
        pass


class Peca(Parte):

    def __init__(self, numero, descricao, custo):
        super().__init__(numero, descricao)
        self.custo = custo

    def aceitar(self, visitante):
        visitante.visitar_peca(self)


class Montagem(Parte):

    def __init__(self, numero, descricao):
        super().__init__(numero, descricao)
        self.partes = []

    def aceitar(self, visitante):
        for parte in self.partes:
            parte.aceitar(visitante)
        visitante.visitar_montagem(self)

    def adicionar(self, nova_parte):
        self.partes.append(nova_parte)


class VisitanteParte(ABC):

    @abstractmethod
    def visitar_montagem(self, montagem):
        pass

    @abstractmethod
    def visitar_peca(self, peca):
        pass


class VisitanteCustoExpandido(VisitanteParte):

    def __init__(self):
        self.custo = 0

    def visitar_peca(self, peca):
        self.custo += peca.custo

    def visitar_montagem(self, montagem):
        pass


# Exemplo de uso
celular = Montagem("CP-7734", "Celular")
tela = Peca("DS-1428", "Tela LCD", 14.37)
alto_falante = Peca("SP-92", "Alto-falante", 3.50)
microfone = Peca("MC-28", "Microfone", 5.30)
radio_celular = Peca("CR-56", "Rádio Celular", 30)
tampa_frontal = Peca("FC-77", "Tampa Frontal", 1.4)
tampa_traseira = Peca("RC-77", "Tampa Traseira", 1.2)
teclado = Montagem("KP-62", "Teclado")
botao = Montagem("B52", "Botão")
capa_botao = Peca("CV-15", "Capa", .5)
contato_botao = Peca("CN-2", "Contato", 1.2)
botao.adicionar(capa_botao)
botao.adicionar(contato_botao)
for _ in range(15):
    teclado.adicionar(botao)
celular.adicionar(tela)
celular.adicionar(alto_falante)
celular.adicionar(microfone)
celular.adicionar(radio_celular)
celular.adicionar(tampa_frontal)
celular.adicionar(tampa_traseira)
celular.adicionar(teclado)

visitante_custo_expandido = VisitanteCustoExpandido()
celular.aceitar(visitante_custo_expandido)
print(visitante_custo_expandido.custo)
