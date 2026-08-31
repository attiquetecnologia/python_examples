# Exemplo: Validação de dados de entrada
senha_correta = "1234"
tentativa = input("Digite a senha: ")
while tentativa != senha_correta:
    print("Senha incorreta. Tente novamente.")
    tentativa = input("Digite a senha: ")
print("Acesso concedido!")
