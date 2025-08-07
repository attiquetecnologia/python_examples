leituras = [
    'branco', 'preto','preto'
    , 'vermelho','vermelho', 'azul','branco','amarelo','branco'
    , 'vermelho', 'vermelho','vermelho', 'preto','azul'
    ]

resgates_detectados = 0
parado = False
i = 0

while i < len(leituras):
    if parado:
        parado = False
        i += 1
        continue

    atual = leituras[i]
    prox = leituras[i+1] if i+1 < len(leituras) else ""
    if atual == 'amarelo':
        parado = True
    if atual == 'vermelho' and prox == 'vermelho':
        resgates_detectados += 1
        i += 2 
    else:
        i += 1
    print("Resgates detectados:", resgates_detectados)