count = []
def login(senha):
    if len(count) == 3:
        return "Bloqueado!"

    if senha == 9343:
        return True
    else:
        count.append(senha)
        return False

tentativa = 0
senha = 0000
while True:
    # Tentativa: 8708, Senha: 8707, Senha incorreta!
    if login(senha):
        print(f"Tentativa: {tentativa}, Senha: {senha}, Senha correta!")
        break
    else:
        print(f"Tentativa: {tentativa}, Senha: {senha}, Senha incorreta!")

    tentativa += 1
    senha +=1