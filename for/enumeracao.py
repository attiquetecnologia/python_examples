"""Dada a lista de convidados 
convidados = ["Alice", "Bob", "Carlos", "Diana", "Eduardo"], 
crie um programa que imprima uma lista numerada no formato:
    1. Alice
    2. Bob
    ... e assim por diante.
"""
convidados: list = ["Alice", "Bob", "Carlos", "Diana", "Eduardo"]
# indice recebe o resultado do enumerate
# convidado recebe os valores da lista
for indice, convidado in enumerate(convidados):
    print(indice, convidado)