"""
Imagine que você recebeu uma lista de preços de produtos: 
precos = [10.50, 150.00, 45.00, 210.90, 85.00, 300.00]. 
Crie um programa que percorra essa lista e gere uma nova 
lista chamada produtos_premium contendo apenas os valores 
acima de R$ 100,00. 
Ao final, exiba a nova lista.
"""
precos = [10.50, 150.00, 45.00, 210.90, 85.00, 300.00]
produtos_premium: list = []
for preco in precos:
    if preco >= 100:
        produtos_premium.append(preco)

print("Produtos Premium", produtos_premium)