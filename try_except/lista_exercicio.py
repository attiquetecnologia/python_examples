
#Erro Simples:
#Escreva um código que tente acessar uma variável não definida dentro de um try...except e exiba uma mensagem personalizada.
try:
    a + 1
except NameError as ex:
    print("Erro", Exception(f"A variável não foi definida {ex}"))

#Divisão Segura:
#Crie uma função que receba dois números e trate o erro caso o denominador seja zero.
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Dominador não pode ser zero")
    return a/b
try:
    divide(10, 0)
except ZeroDivisionError as ex:
    print("Erro capturado: ", ex)
#Validação de Entrada:
#Escreva um código que peça ao usuário um número e trate erros caso ele digite algo inválido.
print("Area retangulo")
try:
    base = int(input("Base: "))
    altura = int(input("Altura: "))
except ValueError as ex:
    print("Informe somente números inteiros:", ex)
#Erro Personalizado:
#Crie uma classe de exceção personalizada chamada ErroIdadeInvalida e use-a para validar 
# se uma idade informada está entre 0 e 120.
class ErroIdadeInvalida(Exception):
    def __init__(self, idade, message="Idade deve ser entre 0-120 anos"):
        super().__init__(f"{message} Valor informado: {idade}")

try:
    idade = int(input("Idade: "))
    if idade <0 or idade > 120:
        raise ErroIdadeInvalida(idade)
except ValueError as ex:
    print(ex)