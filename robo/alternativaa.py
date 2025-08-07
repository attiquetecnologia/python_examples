trilha = ['branco','vermelho','vermelho','amarelo','branco', 'preto', 'preto', 'vermelho', 'branco','vermelho','vermelho']
i = 0
resgates = 0
while i < len(trilha):
    if trilha[i] == 'vermelho' and trilha[i+1] == 'vermelho':
        resgates += 1
        i += 2
    elif trilha[i] == 'preto' and trilha[i+1] == 'preto':
        break
    else:
        i += 1
    print(resgates)