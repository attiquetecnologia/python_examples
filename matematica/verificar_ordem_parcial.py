def verificar_ordem_parcial(matriz):
    n = len(matriz)

    # Verificação da Antissimetria: se M na linha i e coluna j é igual 
    # a 1 e i é diferente de j, então M na linha j e coluna i deve ser 0
    antissimetrica = True
    for i in range(n):
        for j in range(n):
            if i != j and matriz[i][j] == 1 and matriz[j][i] == 1:
                antissimetrica = False
                break
                
    # Verificação da Transitividade: se M na linha i e coluna j 
    # é igual a 1 e M na linha j e coluna k é igual a 1, então M na linha i 
    # e coluna k deve ser 1
    transitiva = True
    for i in range(n):
        for j in range(n):
            if matriz[i][j] == 1:
                for k in range(n):
                    if matriz[j][k] == 1 and matriz[i][k] != 1:
                        transitiva = False
                        break

    return antissimetrica, transitiva