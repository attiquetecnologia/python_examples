nome1 = input("Nome do aluno 1: ")
prova1 = float(input("Nota da prova 1: "))
while prova1 < 0 or prova1 > 10: # Valida prova1
    prova1 = float(input("Digite o valor de 0-10 pra prova1: "))

nome2 = input("Nome do aluno 2: ")
prova2 = float(input("Nota da prova 2: "))
while prova2 < 0 or prova2 > 10: # Valida prova1
    prova2 = float(input("Digite o valor de 0-10 pra prova2: "))

nome3 = input("Nome do aluno 3: ")
prova3 = float(input("Nota da prova 3: "))
while prova3 < 0 or prova3 > 10: # Valida prova1
    prova3 = float(input("Digite o valor de 0-10 pra prova3: "))

aluno = None
maior = None
# Se p1 > 2 e 3 p1 é maior
if prova1 > prova2 and prova1 > prova3:
    maior = prova1
    aluno = nome1

elif prova1 > prova2 and prova1 > prova3:
    maior = prova2
    aluno = nome2

elif prova1 > prova2 and prova1 > prova3:
    maior = prova3
    aluno = nome3

print(f"O aluno {aluno}, teve a maior nota {maior}")