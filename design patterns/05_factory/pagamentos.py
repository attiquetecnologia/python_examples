from pagamento_interface import ServicoPagamentoInterface

class PagamentoPayPal(ServicoPagamentoInterface):

    def pagar(self, valor: float):
        pass

class PagamentoDinheiro(ServicoPagamentoInterface):

    def pagar(self, valor: float):
        pass