c1 = 0
c2 = 0
c3 = 0
c4 = 0
nulo = 0
total = 0
branco = 0
def menu():
    return """
    1 - Sofrencio
    2 - Burraldo
    3 - Xenomorfo
    4 - Alouprei
    5 - Voto branco
    6 - Voto nulo
    0 - Fim da votação
    """
voto = -1
while voto != 0:
    print(menu())
    voto = int(input("Numero: "))
    if voto == 1:
        c1 += 1
    elif voto == 2:
        c2 += 1
    elif voto == 3:
        c3 += 1
    elif voto == 4:
        c4 += 1
    elif voto == 5:
        branco += 1
    elif voto == 6:
        nulo += 1
    else:
        print("Você digitou operação inválida")
print("")
print("="*10)
print("APURAÇÃO DE VOTOS")
print(f"Sofrencio: {c1}")
print(f"Burraldo: {c2}")
print(f"Xenomorfo: {c3}")
print(f"Alouprei: {c4}")
print(f"Brancos: {branco}")
print(f"Alouprei: {nulo}")
total = c1+c2+c3+c4+branco+nulo
print(f"TOTAL DE VOTOS...{total}")
print(f"VOTOS BRANCOS...{branco}")
print(f"VOTOS BRANCOS...{(100*branco/total):,.2f}%")
print(f"VOTOS NULOS...{nulo}")
print(f"VOTOS NULOS...{(100*nulo/total):,.2f}%")
print(f"BRANCOS E NULOS...{nulo+branco}")
print(f"BRANCOS E NULOS...{(100*(nulo+branco)/total):,.2f}%")