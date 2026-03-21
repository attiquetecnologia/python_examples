"""
Escreva um programa que utilize o laço for e a função range() 
para imprimir todos os números múltiplos de 3, no intervalo de 1 a 50, 
em ordem decrescente (do maior para o menor).
"""
for numero in range(50):
    # divisivel por 3
    if numero % 3 == 0: # o resto por 3 tem que ser zero
        print(f"{numero} é multiplo de 3...")