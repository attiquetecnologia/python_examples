from pagamentos import PagamentoDinheiro, PagamentoPayPal
from http_request import HttpRequest

def pagamento_factory(tipo: str):
    match tipo:
        case 'dinheiro':
            
            return PagamentoDinheiro()
        case 'online':
            obj = HttpRequest()
            return PagamentoPayPal(obj)
        case _:
            pass

pagamento = pagamento_factory("online")
pagamento.pagar(555)