# Pegar 5 alunos 
alunos = []
notas = []

for elemento in range(5):
    nome = input("Nome do aluno: ")
    nota = int(input("Nota do aluno: "))
    alunos.append(nome)
    notas.append(nota)

print(alunos)
print(notas)