# Uma pessoa mora na cidade A e deseja viajar para conhecer a cidade C. 
# Para isso, é preciso passar primeiro pela cidade B. 
# Existem 4 caminhos que levam até a cidade B e, a partir da cidade B, 
# três caminhos que levam até a cidade C. Supondo que a única maneira 
# de chegar até a cidade C seja passando por B, de quantas formas 
# diferentes esta pessoa pode ir até à cidade C, e voltar para cidade A?

origem: str = 'A'
destino: str = 'C'
caminhos_B: tuple = (1,2,3,4)
caminhos_C: tuple = (1,2,3)

op: int = 1
for p in range(4):
    for c in range(3):
        print(f"Caminho {op} A:{p+1} -> C:{c+1}")
        op += 1

op = 1
for p in range(3):
    for c in range(2):
        print(f"Caminho {op} C:{p+1} -> A:{c+1}")
        op += 1