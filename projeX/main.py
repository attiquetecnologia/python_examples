from lib.funcoes import criar_conta, mostrar_contas, resgatar, alterar_conta
from dados import contas


# Arquivo principal responsável por conectar todo o sistema

while True:
    print("""
    1 - Criar uma conta   
    2 - Mostrar contas
    3 - Alterar conta
    4 - opção D
    5 - opção E
    0 - Sair
    """)
    opcao: str = input("Opção: ")
    if opcao == '0':
        break
    elif opcao == '1':
        # criar uma conta
        # vamos usar dicionário com variaveis locais
        nome: str = input("Nome da conta: ")
        total: float = 0.0 # iniciando total com 0 sempre
        conta = {
            "nome": nome, "total": total
        }
        resultado = criar_conta(contas, conta)
        novo_id = resultado[1]
        contas = resultado[0]

        # validação se salvar
        if novo_id > 0: 
            print(f"Novo registro adicionado {novo_id}")
            mostrar_contas(contas)
        input("Digite uma tecla para continuar...")
    elif opcao == '2':
        mostrar_contas(contas)
        input("Digite uma tecla para continuar...")
    elif opcao == '3':
        mostrar_contas(contas) # primeiro mostra contas
        id: int = int(input("Digite o ID da conta: ")) # depois seleciona ID
        conta = resgatar(contas, id) # Resgata a conta no banco de dados
        if conta: # Se achar a conta
            # Usando variáveis para auxiliar o processo
            nome = input("Nome da conta [deixe em branco para não alterar] ")
            total = input("Total da conta [deixe em branco para não alterar] ")
            if nome != "":
                conta["nome"] = nome # coloca o novo valor no registro
            if total != "": 
                conta["total"] = total # coloca o novo valor no registro
            # agora chama update para persistir os dados (salvar definitivo)
            contas = alterar_conta(contas, conta)
            mostrar_contas(contas)
        else:
            print(f"Conta {id} não encontrada!")

        input("Digite uma tecla para continuar...")