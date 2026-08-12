def testar_tautologia_de_morgan():
    eh_tautologia = True
    
    for A in [True, False]:
        for B in [True, False]:
            # Lado Esquerdo: not (A and B)
            lado_esquerdo = not (A and B)
            
            # Lado Direito: (not A) or (not B)
            lado_direito = (not A) or (not B)
            
            # Checa se ambos os lados são equivalentes (Bicondicional)
            resultado = (lado_esquerdo == lado_direito)
            
            if not resultado:
                eh_tautologia = False
                
    if eh_tautologia:
        print("A expressão é uma TAUTOLOGIA!")
    else:
        print("A expressão NÃO é uma tautologia.")

testar_tautologia_de_morgan()