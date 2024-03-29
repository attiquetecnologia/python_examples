"""
Usando os conhecimentos sobre dicionário que possui, elabore um programa que 
exiba na tela uma lista de produtos pré-cadastrados e depois permita que o 
usuário compre um dos produtos.
Para comprar o produto ele deve se cadastrar no sistema.
"""

from datetime import datetime

# Funções...
# Incrementar id
def ultimo_id(lista):
    return lista[-1]["id"]

def auto_increment(last_id):
    return last_id + 1

def find(lista, id):
    for l in lista:
        if l['id'] == id:
            return l

def cadastrar_venda(lista):
    cliente = int(input("Id do cliente: "))
    produto = int(input("Id do produto: "))
    qtd = int(input('Quantidade do produto: '))

def exibir(lista):
    for l in lista:
        print(l)  
produtos = [
    {"id": 1, "descricao": "Celular", "preco": 1999.23}
    ,{"id": 109, "descricao": "Computador", "preco": 3999.23}
    ,{"id": 11, "descricao": "Roteador", "preco": 199.23}
]
print( "Ultimo id de produtos é", ultimo_id(produtos) )

clientes = [
    { "id": 1, "nome": "Pessoa001", "telefone": "18 4994 3883"
    , "cpf": "10999", "cep": "14780-000" }
    ,{ "id": 2, "nome": "Pessoa002", "telefone": "18 4194 3883"
    , "cpf": "10899", "cep": "14780-030" }
]
print( "Ultimo id de clientes é", ultimo_id(clientes) )

vendas = [
    {"id": 1, "data": datetime(2024, 2, 26, 13, 10, 23), "cliente_id": 2}
]
print( "Ultimo id de vendas é", ultimo_id(vendas) )

itens_venda = []

print(vendas)
print(datetime.today())

print("Lista de produtos")
print(produtos)

print("Lista de clientes")
print(clientes)

cliente = int(input("Id do cliente: "))
produto = int(input("Id do produto: "))
qtd = int(input('Quantidade do produto: '))

# Criando uma venda
venda = {"id": 2, "data": datetime.today(), "cliente_id": cliente}
vendas.append(venda)
print("Vendas")
print(vendas)

#Buscar valor do produto
for p in produtos:
    if p['id'] == produto:
        produto = p # Subescreve o produto

# Adiciona itens a venda
item = {"id": 1, "venda_id": 2, "produto_id": produto['id']
        , "quantidade": qtd, "valor": produto["valor"] }
itens_venda.append(item)
print(itens_venda)

