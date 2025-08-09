from abc import ABC, abstractmethod
# fontes: https://www.alura.com.br/artigos/design-patterns-python
# https://www.youtube.com/watch?v=bPa6qDnZ-Ck
class ServicoPagamentoInterface(ABC):
    @abstractmethod
    def pagar(self, valor: float):
        # metodo obrigatório no filho
        pass

