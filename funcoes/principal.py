# Crie dois arquivos principal.py e biblioteca.py

# Dentro de biblioteca crie:
# - uma função que receba a idade de uma
# pessoa e exiba uma mensagem formatada.
# "Olá a idade é XYZ."
# - Uma função que recebe dois números e retorne
# para o usuário a data formatada DD/MM/AAAA.
# Exemplo data(10, 9, 2023)

# O arquivo principal deve chamar essas funções
# conforme o usuário pedir
from bibliotecas import idade, data

while True:
    comando = input("$ ")
    if comando == "idade":
        print(idade(input("Qual a idade? ")))
    elif comando == "data":
        dia = input("Dia? ")
        mes = input("Mês? ")
        print(data(dia, mes))
    else:
        break