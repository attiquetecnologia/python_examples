# Dado uma lista com 1000 registros, faça um algorítimo
# para listar os elementos da lista aos poucos conforme
# de 10 em 10 registros

import random
lista = [10, 9, 3, 33, 19, 11, 39, 19, 9, 2, 5, 6, 8, 1, 20]

def paginator(pagina, elementos = 10):
    if pagina>0:
        pagina += elementos
    for l in lista[pagina: elementos]:
        print(l)

if __name__ == "__main__":
    paginator(0)
    print("pagina2")
    paginator(1)