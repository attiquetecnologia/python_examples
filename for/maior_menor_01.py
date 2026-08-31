#-*- coding: utf-8 -*-

valores = [10, 8, 5, 11, 4, 2]
menor = valores[0]
maior = valores[0]
for v in valores:
    if v > maior:
        maior = v
    elif v < menor:
        menor = v

print(f"O maior valor é {maior}")
print(f"O menor valor é {menor}")