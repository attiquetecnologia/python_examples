#-*- coding: utf-8 -*-

def media(dados=[]):
    """ dados: Recebe lista a somar
        return: somatorio/elementos 
    """
    return sum(dados)/len(dados)

valores = [10, 9, 7]
print(f"A média entre 10, 9, 7 é {media(valores)}")

def menu():
    return """
        Menu
        1 - Opção
        2 - Opção
        3 - Sair
    """

print(menu())

def formata(dia, mes, ano):
    print(f"{dia}/{mes}/{ano}")