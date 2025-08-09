from abc import ABC, abstractmethod

class ServicoPagamentoInterface(ABC):
    @abstractmethod
    def pagar(self, valor: float):
        # metodo obrigatório no filho
        pass

        