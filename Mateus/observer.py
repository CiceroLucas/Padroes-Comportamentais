# Importe o módulo Observer do pacote PyPubSub
from pubsub import pub

# Classe do Observador (Cliente)
# Cada objeto cliente tem um nome
class Cliente:
    def __init__(self, nome):
        self.nome = nome

    def receber_notificacao(self, mensagem):
        print(f"{self.nome} recebeu a seguinte mensagem: {mensagem}")

# Classe do Sujeito (Loja)
class Loja:
    def __init__(self):
        # neste construtor, isso permite que outras partes do código se inscrevam para receber notificações 
        # quando o tópico 'nova_promocao' for publicado.

        pub.subscribe(self.notificar_clientes, 'nova_promocao')
        self.clientes = []

    def adicionar_cliente(self, cliente):
        self.clientes.append(cliente)

    def remover_cliente(self, cliente):
        self.clientes.remove(cliente)

         
    def definir_promocao(self, promocao):
        pub.sendMessage('nova_promocao', mensagem=f"Nova promoção: {promocao}")
        # Ele publica uma mensagem no tópico 'nova_promocao',
    
    def notificar_clientes(self, mensagem):
        for cliente in self.clientes:
            cliente.receber_notificacao(mensagem)

        # É chamado quando uma nova promoção é definida.

# Criamos uma instância da classe Loja chamada loja.
if __name__ == "__main__":
    loja = Loja()
    
    # 3 instancias
    cliente1 = Cliente("Mateus")
    cliente2 = Cliente("Arthut")
    cliente3 = Cliente("Bruno")
    
    loja.adicionar_cliente(cliente1)
    loja.adicionar_cliente(cliente2)
    loja.adicionar_cliente(cliente3)
    
    loja.definir_promocao("Desconto de 20% em todos os produtos!")
    
    loja.remover_cliente(cliente2)
    
    loja.definir_promocao("Oferta relâmpago: compre 1, leve 2!")
