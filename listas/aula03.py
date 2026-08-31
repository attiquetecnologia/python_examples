"""Descricao: exercícios da aula 03 sobre listas, tuplas e conjuntos 
nome_arquivo: aula03.py 
nome_exercicio: Aula 03 
nome_aluno: Professor Attique
email_aluno: rodrigoatique@gmail.com 
turma: DSM 2T2026
"""

# Crie uma lista que armazene 10 nomes de pessoas e depois
#  exiba na tela somente os nomes cujos indices sejam impares (sem usar laços).

nomes = ['Maria', 'João', 'Esterlucia', 'Cremilda', 'Fravio', 'Agildo', 'Neymar', 'Romilson'
         , 'Ednaldo', 'Nomelinda']

print(1, nomes[1])
print(3, nomes[3])
print(5, nomes[5])

for indice, nome in enumerate(nomes):
    if indice % 2 != 0:
        print(indice, nome)

print(20*'-')

indice: int = 0
while indice < len(nomes):
    if indice % 2 != 0:
        print(indice, nomes[indice])
    indice += 1 # incrementa 1 ao indice


print(20*'=')
# Crie uma lista para armazenar 10 números e depois exiba:
#  Quantos números foram armazenados, 
# o cálculo da soma de todos os números e a média de todos os números.
numeros = [1,2,4,5,6,8,9,9,10,11]
print(f"Foram armazenados {len(numeros)} números.")
print(f"Somatório: {sum(numeros)}.")
print(f"Média {sum(numeros)/len(numeros)}.")

print(20*'=')
# Crie uma lista com 5 frutas e depois exibe em ordem alfabética 
# crescente e decrescente.
frutas = ['Maçã', 'Banana', 'Pera', 'Abacaxi', 'Melão']
print(f"Desordenado {frutas}")
frutas.sort()
print(f"Ordem Crescente {frutas}")
frutas.reverse()
print(f"Ordem Decrescente {frutas}")

print(20*'=')
# Peça uma data ao usuário no formato “dd/mm/aaaa” usando 
# o método split exiba na tela Dia: dd, Mês: mm e Ano: aaaa.
dia = input("Digite a data de hoje no formato dd/mm/aaaa: ")
dia = dia.split('/')
print(type(dia))
print(f"Dia: {dia[0]}, Mês: {dia[1]}, Ano: {dia[2]}")

print(20*'=')
estados = 'SP', 'RJ', 'MG', 'ES', 'PR', 'SC', 'RS'
# estados.remove('PI')

print(20*'=')
# 6) Dada a tupla heterogênea: ‘Hamburger’, 10.9, ‘Pastel’, 
# 11.99 ‘Salgado’, 6.99. Crie sub tuplas para agrupar o lanche com o preço.
cardapio = ('Hamburger', 10.9, 'Pastel', 11.99, 'Salgado', 6.99)
# ele pode combinar tudo em uma lista de tuplas
novo_cardapio = []
aux = ()
for c in cardapio:
    # o primeiro é sempre string
    aux = c, # inicia a tupla com variavel auxiliar
    if isinstance(c, float):
        aux = aux, c # repete aux
        novo_cardapio.append(aux)
        aux = () # zera
print(novo_cardapio) # Exercicio incompleto

# cardapio = [('Hamburger', 10.9), ('Pastel', 11.99), ('Salgado', 6.99), ]
