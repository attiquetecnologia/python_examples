# Vamos implementar os requisitos:
# RF018 - Somente usuários cadastrados devem acessar o sistema;
# RN015 - A senha deve ser bloqueada na 3 tentativa errada do usuário;

print("*** Faça login no sistema ***\n")

# Dicionário contendo chave: username e valor: senha
usuarios: dict = {'aluno_senai': '1234', 'valeu':'00289'
                  , 'bojao_cromado': 'pokebola'
                  , 'bataman': 'coringa'}

tentativa = 0 # tentativas de acesso

# Laço para tentativas
for tentativa in range(3):
    # Pega dados do usuário
    username: str = input("Usuário: ")
    senha: str = input("Senha: ")
    # Processa com if e while
    if username in usuarios and usuarios.get(username) == senha:
        print("Usuário logado com sucesso!!!")
        break # quebra o loop
    else:
        print("Usuário ou Senha incorretos!")
        tentativa += 1

if tentativa == 3:
    print("Usuário bloqueado!")