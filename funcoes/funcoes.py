#-*- coding: utf-8 -*-

def media(dados=[]):
    """ dados: Recebe lista a somar
        return: somatorio/elementos 
    """
    return sum(dados)/len(dados)

def menu():
    return """
        Menu
        1 - Opção
        2 - Opção
        3 - Sair
    """

def formata(dia, mes, ano):
    return f"{dia}/{mes}/{ano}"

def formato_moeda(valor):
    valor = "R$ {:.2f}".format(valor)
    # troca ponto por virgula
    valor = valor.replace(".", ",")
    return f"{valor}"

def area_total(largura, altura):
    return largura*altura
