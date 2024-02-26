"""
Usando os conhecimentos sobre dicionário que possui, elabore um programa que 
exiba na tela uma lista de produtos pré-cadastrados e depois permita que o 
usuário compre um dos produtos.
Para comprar o produto ele deve se cadastrar no sistema.
"""

carrinho = [] # Armazena os produtos comprados
produtos = [
    {"id": 1, "descricao": "Celular", "preco": 1999.23}
    ,{"id": 109, "descricao": "Computador", "preco": 3999.23}
    ,{"id": 11, "descricao": "Roteador", "preco": 199.23}
]
cliente = {

}

produtos_cliente = [
    {"id":1, "id_cliente": 1, "id_prouto": 109, 'qtd': 2,}
]

print("Escolha um produto")
for i in range(len(produtos)):
    print(produtos[i])