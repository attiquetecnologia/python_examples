
# Escrita de arquivos

# Dado um arquivo dados.json faça um algoritimo para criar o arquivo e salvar
# os dados da lista dentro dele.

# NOTA: O arquivo dados.json será criado na raiz do projeto

import json # importa biblioteca do json

dados = [ {"id": 10, "datahora": "2024-03-02T10:23:39", "temperatura": 23.9} ]

with open("dados.json", "w") as file: # abre o arquivo no modo append (acrescentar)
    file.write(json.dumps(dados)) # escreve no arquivo convertendo dicionário em json

# Leitura de arquivos
# Dado um arquivo dados.json faça um algoritimo para abir e printar na tela seu conteúdo
with open("dados.json", "r") as file: # abre o arquivo em modo leitura (read)
    read = file.read()
    print(read)

# Manipulando e alterando arquivos
# Faça um algoritimo que leia o arquivo dados.json e acrescente mais um elemento a lista de 
# medições

# Precisamos de algumas bibliotecas para nos auxiliar...
import os, sys
sys.path.insert(0,os.path.abspath(os.curdir))

from funcoes.funcoes import ultimo_id # reaproveitando código de outro exemplo
dados: list = []
reg: dict = {}

with open("dados.json", "r") as file: # Primeiro abre para leitura
    # Estamos trabalhando com o padrão JSON
    dados = json.loads(file.read()) # abre e converte a string do read() para dicionário
    print(dados, type(dados)) # agora estamos manipulando uma lista de dicionários
    
    from datetime import datetime # biblioteca de manipular datas

    reg: dict = {"id": ultimo_id(dados)+1, "datahora": datetime.now(), "temperatura": 22.9}

with open("dados.json", "w") as file: # vamos abir o arquivo no modo escrita para subitituir todo seu conteúdo
    # agora adiciona o registro aos dados
    dados.append(reg)
    file.write(json.dumps(dados, indent=4, sort_keys=True, default=str)) # salva novamente no arquivo

with open("dados.json", "r") as file: # abre o arquivo em modo leitura (read)
    read = file.read()
    print(read)


# As operações para esse arquivo estão muito trabalhosas e exige muito retrabalho
# Crie uma função para fazer a leitura do conteúdo do arquivo json e retornar uma lista de
# dicionários
# Crie outra função para adicionar registros ao arquivo de dados.