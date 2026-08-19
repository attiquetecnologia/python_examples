# Busca por um número par na lista
numeros = [1, 3, 5, 7]
for num in numeros:
    if num % 2 == 0:
        print(f"Número par encontrado: {num}")
        break
else:
    print("Nenhum número par foi encontrado na lista.")
