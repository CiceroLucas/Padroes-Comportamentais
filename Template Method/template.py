from abc import ABC, abstractmethod

class Template(ABC):
    def template_method(self):
        self.step1()
        self.step2()

    @abstractmethod
    def step1(self):
        pass

    @abstractmethod
    def step2(self):
        pass

class ConcreteClass(Template):
    def step1(self):
        print("Passo 1 executado")

    def step2(self):
        print("Passo 2 executado")

# Uso do Template Method
obj = ConcreteClass()
obj.template_method()
