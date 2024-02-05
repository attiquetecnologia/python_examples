# Faça um programa que receba números inteiros e pare 
# somente quando o número atual for menor que o anterior.

numero = int(input("Digite um número: "))
while True:
    novo = int(input("Digite outro número: "))
    if novo > numero:
        novo = numero
    else:
        print(f"Número menor que {numero}")
        break