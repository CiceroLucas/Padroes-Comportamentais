class Handler:
    def __init__(self, successor=None):
        self.successor = successor

    def handle_request(self, request):
        if self.successor:
            self.successor.handle_request(request)

class ConcreteHandlerA(Handler):
    def handle_request(self, request):
        if request == 'A':
            print("Handler A processou a solicitação")
        else:
            super().handle_request(request)

class ConcreteHandlerB(Handler):
    def handle_request(self, request):
        if request == 'B':
            print("Handler B processou a solicitação")
        else:
            super().handle_request(request)

# Uso do Chain of Responsibility
handler_a = ConcreteHandlerA()
handler_b = ConcreteHandlerB()
handler_a.successor = handler_b

handler_a.handle_request('A')  # Será processado por Handler A
handler_a.handle_request('B')  # Será processado por Handler B
handler_a.handle_request('C')  # Não será processado por nenhum handler
