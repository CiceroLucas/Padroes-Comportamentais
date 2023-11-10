# Interface Command
# ele possui um metedo execute, que sera implementado pelos comando concretos para realizar as ações.
class Command:
    def execute(self):
        pass

# Receptor
# O Light é o Receptor, que é responsável por realizar a ação real, neste caso, ligar e desligar a luz. 
# Ele possui dois métodos, on e off, que são as ações que queremos encapsular em comandos.
class Light:
    def on(self):
        print("Luz ligada")

    def off(self):
        print("Luz desligada")

# definindo os comandos  LightOnCommand e LightOffCommand.
# Cada comando concreto herda da interface Command e implementa o método execute.
# Eles encapsulam as ações de ligar e desligar a luz, chamando os métodos correspondentes no Receptor.
class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.on()

class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.off()

# Invoker
# Ela inicializa uma variável self.command como None, o que significa que inicialmente 
# não há comando atribuído a este controle remoto.
class RemoteControl:
    def __init__(self):
        self.command = None

# atribuir um comando específico ao controle remoto.
# isso permite que o invocador saiba qual comando deve ser executado.
    def set_command(self, command):
        self.command = command


# é responsável por executar o comando atualmente atribuído ao controle remoto.
    def press_button(self):
        self.command.execute()

# Client
if __name__ == "__main__":
    # criamos uma instância do receptor, no caso, a light, que representa a lâmpada que queremos controlar.
    light = Light()
    # criamos instâncias dos comandos light_on e light_off
    # Cada comando concreto é associado ao Receptor (light) no momento da criação, para que saibam qual ação executar.
    light_on = LightOnCommand(light)
    light_off = LightOffCommand(light)

    # Cria instância do Invoker (RemoteControl)
    # que é o controle remoto que permite que o usuário defina e execute comandos.
    remote = RemoteControl()

    # Define o comando desejado no invoker
    remote.set_command(light_on)

    # Pressiona o botão no invoker para executar o comando
    remote.press_button()

    remote.set_command(light_off)
    remote.press_button()