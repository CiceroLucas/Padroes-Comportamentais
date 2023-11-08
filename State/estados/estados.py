from .interface import IEstado

class EstadoLiquido(IEstado):

    def esquentar(self):
        return EstadoGasoso()
    
    def esfriar(self):
        return EstadoSolido()
    
class EstadoSolido(IEstado):

    def esquentar(self):
        return EstadoLiquido()
    
    def esfriar(self):
        return EstadoSolido
    
class EstadoGasoso(IEstado):
    
    def esquentar(self):
        return EstadoGasoso()
    
    def esfriar(self):
        return EstadoLiquido()