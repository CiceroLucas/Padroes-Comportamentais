class Parte:

    def _init_(self, numero, descricao):
        self.numero = numero
        self.descricao = descricao


class Peca(Parte):

    def _init_(self, numero, descricao, custo):
        super()._init_(numero, descricao)
        self.custo = custo

    def aceitar(self, v):
        v.visitarPeca(self)


class Montagem(Parte):

    def _init_(self, numero, descricao):
        super()._init_(numero, descricao)
        self.partes = []

    def aceitar(self, v):
        v.visitarMontagem(self)

    def adicionar(self, nova_parte):
        self.partes.append(nova_parte)


class VisitanteParte:
    def visitarMontagem(self, m):
        for p in m.partes:
            p.aceitar(self)


class VisitanteCustoExpandido(VisitanteParte):

    def _init_(self):
        self.custo = 0

    def visitarPeca(self, p):
        self.custo += p.custo


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

v = VisitanteCustoExpandido()
celular.aceitar(v)
print(v.custo)
