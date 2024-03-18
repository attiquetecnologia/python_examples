# Dado um caractere digitado pelo usuário é preciso garantir que
# sempre seja digitado um número inteiro e positivo

try: # Tente
    valor: int = int(input("Valor: ")) # já converte para int
    while valor < 0:
        valor = int(input("Valor: ")) # já converte para int
except Exception as ex: # Se der erro de conversão
    print(ex)

# >>> Valor: a
# invalid literal for int() with base 10: 'a'
    
