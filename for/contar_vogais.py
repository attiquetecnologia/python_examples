"""
Crie um programa que receba uma frase do usuário e conte quantas 
vogais (a, e, i, o, u) ela possui. 
O programa deve exibir o total ao final.
"""
frase: str = input("Digite uma frase: ")
# Tupla com vogais
vogais: tuple = ('a', 'e', 'i', 'o', 'u')

contador = 0 # contador de vogais
# percorre cada caractere da frase
for f in frase:
    # Se f estiver em vogais...
    if f in vogais:
        contador += 1 # incrementa contador de um em um

# Exibe mensagem
print(f"A frase digitada possui {contador} vogais.")