from src import LutaArco, LutaEspada, Curar, Guerreiro

cavaleiro = Guerreiro(LutaEspada(7))
cavaleiro.acao()
cavaleiro.nivel()

arqueiro = Guerreiro(LutaArco(6))
arqueiro.acao()
arqueiro.nivel()

curandeiro = Guerreiro(Curar(9))
curandeiro.acao()
curandeiro.nivel()