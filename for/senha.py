"""
Faça um programa que armazene uma senha em uma variável e
 de ao usuário 3 tentativas para acertar a senha. 
 O programa deve exibir o número de tentativas que restam 
 para ele acertar até chegar a 3. Se ele acertar dentro 
 das 3 tentativas exibir uma mensagem “Logado com sucesso!”
"""

senha = 'abacaxi'
for p in range(3):
    senha_digitada = input("Qual é a senha: ")
    if senha == senha_digitada:
        print("Logado com sucesso!")
        break
    else:
        if p==2:
            print("Senha incorreta!\nTentativas esgotadas.")
        else:
            print(f"Senha incorreta!\nVocê tem mais {2-p}")