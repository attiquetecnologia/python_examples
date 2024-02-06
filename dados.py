alunos = {
    10: {"nome": "Batman", "t": 9.1, "p1": 8.5, "p2": 9}
    ,11: {"nome": "Robin", "t": 10, "p1": 9.5, "p2": 10}
    ,12: {"nome": "Volverine", "t": 6, "p1": 7, "p2": 8}
    ,13: {"nome": "Gibak", "t": 8, "p1": 9.5, "p2": 10}
}

def media_p(t, p1, p2):
    return t*.3 + p1*.35 + p2*.35

def relatorio():
    aprovados, reprovados, recuperacao = [], [], []

    for k,v in list(alunos.items()):
        media = media_p(v['t'], v['p1'], v['p2'])
        if media >= 7:
            aprovados.append(k)
        elif media <3:
            reprovados.append(k)
        else:
            recuperacao.append(k)
    print(f"Alunos aprovados {len(aprovados)}")
    for p in aprovados:
        print(alunos[p]["nome"])
    print(f"Alunos em recuperação {len(recuperacao)}")
    for p in recuperacao:
        print(alunos[p]["nome"])
    print(f"Alunos reprovados {len(reprovados)}")
    for p in reprovados:
        print(alunos[p]["nome"])            

usuario = input("Usuario: ")
senha = input("Senha: ")
if usuario == "batman" and senha == "osmose":
    relatorio()
else:
    print("Usuario e senha incorretos!")