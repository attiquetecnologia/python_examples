from datetime import date
status = {"ap": "A pagar", "pg": "Pago"}
desp_fixas = [
    {"data": date(2024, 1, 20), "valor": 984.99, "descricao": "Aluguel", "status": "ap"}
    ,{"data": date(2024, 1, 5), "valor": 204.44, "descricao": "Energia", "status": "pg"}
    ,{"data": date(2024, 1, 20), "valor": 84.19, "descricao": "Agua", "status": "ap"}
    ,{"data": date(2024, 1, 10), "valor": 184.99, "descricao": "Mercado", "status": "pg"}
]

desp_variavel = [
    {"data": date(2024, 1, 1), "valor": 294.99, "descricao": "Combustível", "status": "pg"}
    ,{"data": date(2024, 1, 5), "valor": 14.44, "descricao": "Lâmpada", "status": "pg"}
    ,{"data": date(2024, 1, 20), "valor": 200.00, "descricao": "Concerto", "status": "ap"}
    ,{"data": date(2024, 1, 10), "valor": 84.99, "descricao": "Mouse/Teclado", "status": "pg"}
]

receitas = [
    {"data": date(2024, 1, 20), "valor": 1854.99, "descricao": "Salário", "status": "ap"}
    ,{"data": date(2024, 1, 5), "valor": 204.44, "descricao": "Venda Queijo", "status": "pg"}
]

def calc_desp(desp, status):
    soma = 0.0
    for d in desp:
        if status == d['status']:
            soma = d['valor'] + soma
    return soma

def print_despesa():
    desp_fixa_ap = calc_desp(desp_fixas, "ap")
    desp_variavel_ap = calc_desp(desp_variavel, "ap")
    receita = calc_desp(receitas, 'pg')
    resto = desp_variavel_ap+desp_fixa_ap

    print("Exibindo total de receitas e despesas")
    print("Despesas Fixas", "Despesas Variaveis")
    print(str(desp_fixa_ap)+" "*7, desp_variavel_ap)

if __name__== "__main__":
    print_despesa()