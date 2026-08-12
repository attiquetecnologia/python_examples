# Definindo os valores lógicos de A e B
A = True
B = False

# Operações Lógicas
negacao_A = not A
conjuncao = A and B
disjuncao = A or B
condicional = (not A) or B  # Equivalência: A -> B é o mesmo que (not A) or B
bicondicional = A == B      # Equivalência: A <-> B

print(f"A: {A}, B: {B}")
print(f"NOT A: {negacao_A}")
print(f"A AND B (Conjunção): {conjuncao}")
print(f"A OR B (Disjunção): {disjuncao}")
print(f"A -> B (Condicional): {condicional}")
print(f"A <-> B (Bicondicional): {bicondicional}")