"""
Você foi chamado para resolver um problema onde é preciso calcular as despesas
de uma pessoa.
1 - Você precisa exibir de forma ordenada e separada as despesas pagas e a pagar.
    a) utilize um \n, para pular linhas;
    b) "R$ %.2f" % valor, para formato de moeda
    c) print("Data"+" "*6, "Descrição"+" "*5, "Valor"), para o cabeçalho da coluna

2 - Utilize funções criadas por você para reutilizar código e ajudar na produtividade

Exemplo de saída:
EXIBINDO O TOTAL DE DESPESAS PAGAS

Data       Descrição      Valor
2024-01-20 Aluguel        R$ 984.99
2024-01-05 Energia        R$ 204.44
            ...    
2024-01-10 Mouse/Teclado  R$ 84.99
Total ___________________ R$ 1269.18
"""
from datetime import date

status = {"ap": "A pagar", "pg": "Pago"}

desp_fixas = [
    {"data": date(2024, 1, 20), "valor": 984.99, "descricao": "Aluguel", "status": "ap"}
    ,{"data": date(2024, 1, 5), "valor": 204.44, "descricao": "Energia", "status": "pg"}
    ,{"data": date(2024, 1, 20), "valor": 84.19, "descricao": "Agua", "status": "ap"}
    ,{"data": date(2024, 1, 10), "valor": 184.99, "descricao": "Mercado", "status": "pg"}
    ,{"data": date(2024, 1, 1), "valor": 294.99, "descricao": "Combustível", "status": "pg"}
    ,{"data": date(2024, 1, 5), "valor": 14.44, "descricao": "Lâmpada", "status": "pg"}
    ,{"data": date(2024, 1, 20), "valor": 200.00, "descricao": "Concerto", "status": "ap"}
    ,{"data": date(2024, 1, 10), "valor": 84.99, "descricao": "Mouse/Teclado", "status": "pg"}
]

def calc_desp(desp, status):
    soma = 0.0
    for d in desp:
        if status == d['status']:
            soma = d['valor'] + soma
    return soma

def print_despesa(desp, status):
    if status == 'pg': 
        print("EXIBINDO O TOTAL DE DESPESAS PAGAS\n")
    elif status == 'ap':
        print("EXIBINDO O TOTAL DE DESPESAS A PAGAR\n")

    header = "Data"+" "*6+" Descrição"+" "*5+" Valor"
    print(header)
    for d in desp:
        count = len(d["descricao"])
        print(d["data"], d["descricao"]+" "*(14-count), "R$ %.2f" % d["valor"])

    print("Total "+"_"*(len(header)-12), "R$ %.2f" % calc_desp(desp, status))

if __name__== "__main__":
    print_despesa(desp_fixas, 'pg')
    print("-"*50)
    print_despesa(desp_fixas, 'ap')