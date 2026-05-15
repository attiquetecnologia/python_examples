# Exercício 01
# Leia um número inteiro, se o usuário digitar menos 
# um exiba a # mensagem “Saíndo do sistema”, 
# se não “Ok vamos lá”;
numero = int(input("Digite um número: "))
if numero == -1:
    print("Saindo do sistema...")
else:
    print("Ok lets go!")

# Exercício 02
nota = float(input("Digite uma entre 0-10: "))
if nota >= 7.0:
    print("Aprovado!!!!!!!!!!!!!!!")
elif nota >= 4.0:
    print("Recuperação.")
else:
    print("Reprovado.")

# Exercicio 03
nome = input("Diga seu nome: ")
contagem: int = len(nome) # conta caracteres
print("N° de caracteres:", contagem)
if contagem % 2 == 0:
    print("Par")
else:
    print("Impar")