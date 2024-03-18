# Aqui vamos colocar todas as operações CRUD.
# Vale ressaltar que este arquivo não importa nada mas
# apenas será importado no arquivo main para ser usado
# quando for preciso

# ultimo id
def ultimo_id(dados: list)->int:
    ultimo_id = 0
    for d in dados:
        if d["id"] > ultimo_id:
            ultimo_id = d["id"]

    return ultimo_id

def formato_moeda(valor: float) -> str:
    valor = "R$ {:.2f}".format(valor)
    # troca ponto por virgula
    valor = valor.replace(".", ",")
    return f"{valor}"

# Criar nova conta
def criar_conta(contas: list, conta: dict) -> tuple:
    """
        CREATE
        contas: lista de contas
        conta: Dicionário de contas {"nome": "ACcount name"...}
        return: Retorna uma tupla com a lista de contas atualizada
            e o id gerado (contas, novo_id) 
    """
    # passa contas para descobrir o ultimo id
    novo_id = ultimo_id(contas)+1
    conta["id"] = novo_id
    
    contas.append(conta)
    return (contas, novo_id)

def mostrar_contas(contas: list) -> None:
    """
    FindALL
    contas: lista de contas
    return: Exibe uma lista de contas tabuladas
    """
    print("ID", "NOME"+" "*20, "TOTAL")
    for c in contas:
        print("{:0>2}".format(c["id"])
              , c["nome"]+" "*(24-len(c["nome"])) # Preciso saber quantas colunas descrição ocupa e depois subtrair do numero de caracteres que descrição tem
              , formato_moeda(float(c["total"]))
        )

def resgatar(contas: list, id: int) -> dict:
    """
    READ
    contas: lista de contas
    id: id da conta
    return: Devolve a conta encontrada
    """
    for c in contas:
        if c["id"] == id:
            return c # se achar devolve o dict
    return None # Se não retorna None (nenhum)

# Alterar conta
def alterar_conta(contas: list, conta: dict) -> list:
    """
        UPDATE
        contas: lista de contas
        conta: Dicionário de contas {"nome": "ACcount name"...}
        return: Retorna uma tupla com a lista de contas atualizada 
    """
    # Primeiro preciso descobrir a posição do registro na lista
    antigo = resgatar(contas, conta["id"])
    indice = contas.index(antigo) # index é um metodo nativo de listas
    contas[indice] = conta # subistitui registro antigo na posição
    return contas