# Faça um algoritimo que dado uma lista exiba quais
# são os números impares da lista

numeros: list = [10, 21, 4, 9, 10, 99, 100, 101]
for element in numeros:
    if element % 2 != 0:
        print(f"{element} é ímpar!")