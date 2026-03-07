# Exercício 01 - Escreva um programa que receba uma frase do utilizador 
# e imprima o número total de caracteres (incluindo espaços).
print("\nExercício 01")
frase = input("Digite uma frase curta: ")
print(f"Sua frase tem {len(frase)} caracteres.")

# Exercicio 02 - Crie um programa que peça ao utilizador uma 
# palavra e a exiba de três formas:
# Totalmente em maiúsculas.
# Totalmente em minúsculas.
# Apenas com a primeira letra em maiúscula.
print("\nExercício 02")
palavra = input("Digite uma palavra: ")
print(palavra.upper(), palavra.lower(), palavra.capitalize())

# Exercicio 03 - Escreva um programa que peça uma frase e, 
# em seguida, peça uma única letra. O programa deve dizer 
# quantas vezes essa letra aparece na frase informada.
print("\nExercício 03")
letra = input("Digite uma letra: ")
print(f"A letra {letra} aparece {frase.count(letra)} vezes na frase '{frase}'.")

# Crie um programa que receba o nome completo de uma pessoa e o 
# exiba de trás para frente (invertido).
print("\nExercício 04")
nome_completo: str = input("Nome Completo: ")
print(nome_completo[::-1])

print("\nExercício 05")
# Escreva um programa que tenha uma frase fixa 
# (ex: "Eu gosto de programar em Java"). Peça ao utilizador 
# para digitar uma nova linguagem e substitua 
# "Java" pelo valor digitado, exibindo a nova frase.
frase = "Eu gosto de programar em Java!"
print(frase)
linguagem = input("Diga qual linguagem favorita? ")
linguagem = linguagem.replace("Java", "Python")
print(linguagem)

