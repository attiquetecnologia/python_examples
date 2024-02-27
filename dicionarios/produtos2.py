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
    # forma incorreta pois não descobre qual o maior valor
    # return lista[-1]["id"]
    ids = [] # lista temporária para armazenar os ids da lista
    for l in lista:
        ids.append(l['id'])

    return max(ids) # Agora sim retorna o maior id

def auto_increment(last_id):
    return last_id + 1

def find(lista, id): # Recebe a lista e o id do item
    for l in lista: # Percorre a lista
        if l['id'] == id: # Se o id for igual ao da lista
            return l # Retorna a linha atual

def cadastrar_venda(vendas, produtos):
    # Pede os dados pro usuário primeiro
    cliente = int(input("Id do cliente: "))
    produto = int(input("Id do produto: "))
    qtd = int(input('Quantidade do produto: '))
    
    # Resgata o produto
    produto = find(produtos, produto) # coloca novo produto na variável

    novo_id = ultimo_id(vendas)+1

    venda = {"id": novo_id, "data": datetime.today(), "cliente_id": cliente}
    itens_venda = []

    item = {"id": 1, "venda_id": novo_id, "produto_id": produto['id']
        , "quantidade": qtd, "valor": produto["valor"] }
    itens_venda.append(item) # Adiciona item a lista
    venda["items"] = itens_venda # cria nova chave com itens para a venda

    vendas.append(venda) # adiciona nova venda na lista

    vendas.append(venda)

def exibir(lista): # Recebe a lista
    for l in lista: # Percorre a lista
        print(l) # Exibe linha por linha

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

print("Lista de produtos")
print(exibir(produtos))

print("Lista de clientes")
print(exibir(clientes))

# Criando uma venda
# venda = {"id": 2, "data": datetime.today(), "cliente_id": cliente}

# Adiciona itens a venda
# item = {"id": 1, "venda_id": 2, "produto_id": produto['id']
#         , "quantidade": qtd, "valor": produto["valor"] }


