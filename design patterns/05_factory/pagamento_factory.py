from pagamentos import PagamentoDinheiro, PagamentoPayPal

def pagamento_factory(tipo: str):
    match tipo:
        case 'dinheiro':
            return PagamentoDinheiro()
        case 'online':
            return PagamentoPayPal()
        case _:
            pass

    