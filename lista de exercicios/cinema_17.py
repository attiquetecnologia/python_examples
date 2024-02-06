def dados_cinema():
    import random
    dados = []
    notas = ('A','B', 'C', 'D', 'E', 'F')
    for p in range(100):
        dados.append((random.choice(notas), random.randint(15,49)))

    return dados

# print(dados_cinema())

def dados_agencia():
    dados = [] # (código, funcionarios, grande, )
    for p in range(1000):
        funcionarios = random.randint(1,1000)
        if funcionarios < 10:
            dados.append((p, funcionarios, 'micro'))
        elif funcionarios > 10 and funcionarios <= 50:
            dados.append((p, funcionarios, 'pequena'))
        elif funcionarios > 50 and funcionarios < 100:
            dados.append((p, funcionarios, 'média'))
        else:
            dados.append((p, funcionarios, 'grande'))
    return dados