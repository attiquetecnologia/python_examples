# Primeiro programa
print("Hello World!")

# Exercicio 01
x = int(input("Digite um número: "))
print("O número informado foi,", x, ".")

# Exercicio 02
numero1: int = int(input("Digite um número 01: "))
numero2: int = int(input("Digite um número 02: "))
soma: int = numero1 + numero2 # operação soma
print(f"A soma de {numero1} e {numero2} é {soma}.")

# Exercicio 03
numero1: int = int(input("Digite um número 01: "))
numero2: int = int(input("Digite um número 02: "))
numero3: int = int(input("Digite um número 03: "))
numero4: int = int(input("Digite um número 04: "))
soma: int = numero1 + numero2 + numero3 + numero4
media: int = soma/4
print(f"""A média entre {numero1}, {numero2}
      ,{numero3}, {numero4} é {media}.""")

# Exercicio 04
lado = int(input("Digite um lado do quadrado: "))
print("O dobro da área do quadrado é,", lado*lado*2)