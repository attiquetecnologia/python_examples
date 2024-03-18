#programa média
nome: float = input("Diga seu nome: ")
prova1: float = float(input("Nota da prova 1: "))
if prova1 < 0 or prova1 > 10: # Valida prova1
    prova1 = float(input("Digite o valor de 0-10 pra prova1: "))

prova2: float = float(input("Nota da prova 1: "))
if prova2 < 0 or prova2 > 10: # Valida prova1
    prova2 = float(input("Digite o valor de 0-10 pra prova2: "))

trabalho: float = float(input("Nota da prova 1: "))
if trabalho < 0 or trabalho > 10: # Valida prova1
    trabalho = float(input("Digite o valor de 0-10 pra trabalho: "))

# Faça as outras pra prova1 e trabalho
    
media: float = prova1*0.35 + prova2*0.35 + trabalho*0.3

if media>=5:
    situacao: str = "Aprovado!"
elif media > 3.5:
    situacao: str = "Recuperação!"
else:
    situacao: str = "reprovado!"

print(f"Olá, {nome} sua média final é {media}. Situação {situacao}.")