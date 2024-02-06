#-*- coding: utf-8 -*-

alunos = []
for p in range(10):
    nome = input("Nome do aluno: ")
    alunos.append(nome)
print(alunos)
nome = input("Nome do aluno remover: ")
alunos.remove(nome)
print(alunos)