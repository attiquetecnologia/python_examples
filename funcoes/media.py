def media(dados=[]):
    return sum(dados)/len(dados)

valores = [10, 9, 7]
print(f"A média entre 10, 9, 7 é {media(valores)}")

def menu():
    return """
    1 - Calcular média
    2 - Opção 2
    0 - Sair
    """

print(menu())
op = int(input(": "))
if op == 1:
    valores = []
    for p in range(5):
        valor = int(input(f"valor {p+1}: "))
        valores.append(valor)
    print(media(valores))