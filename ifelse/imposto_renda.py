# Faça um programa que receba o nome e o salário 
# de um trabalhador e retorne quanto ele pagará 
# de imposto de renda.
# A tabela de imposto de renda é:
# Até R$ 2112.00 - isento
# De 2.112,01 até 2.826,65 - 7.5%

# De 2.826,66 até 3.751,05  - 15%

# De 3.751,06 até 4.664,68 - 22.5%
# Acima de 4665 - 27,5%

nome: str = input("Seu nome: ")
salario: float = float(input("Qual seu salário bruto: "))
if salario <= 2112.0:
    print("Isento")
elif salario > 2112.0 and salario <=2826.65:
    print(f"Aliquota de 7,5% {salario*.075}")