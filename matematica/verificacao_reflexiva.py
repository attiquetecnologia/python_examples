def verificar_reflexiva(conjunto, relacao):
    tamanho = len(conjunto)
    mapa_indices = {elem: i for i, elem in enumerate(conjunto)}

    # Construção da matriz de relação (inicializada com 0)
    matriz = [[0] * tamanho for _ in range(tamanho)]
    for a, b in relacao:
        if a in mapa_indices and b in mapa_indices:
            matriz[mapa_indices[a]][mapa_indices[b]] = 1

    # Verificação da propriedade reflexiva na diagonal principal
    eh_reflexiva = all(matriz[i][i] == 1 for i in range(tamanho))

    return matriz, eh_reflexiva