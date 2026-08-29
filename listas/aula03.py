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