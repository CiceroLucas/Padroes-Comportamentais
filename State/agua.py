from estados import EstadoLiquido

class Agua:
    def __init__(self):
        self.state = EstadoLiquido()

    def esquentar(self):
        self.state = self.state.esquentar()

    def esfriar(self):
        self.state = self.state.esfriar()

    def __repr__(self):
        return f'Agua(estado={self.state})'