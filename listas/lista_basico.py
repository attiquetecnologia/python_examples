alunos = ["João", "Maria", "Pedro", "Paulo", "Tiago"]
print(alunos) # exibe todos os alunos
print(alunos[2]) # exibe somente o Pedro
print(alunos[-1]) # exibe o Tiago
print(alunos[1:3]) # exibe Maria e Pedro

alunos.append("Patrícia") # Adiciona a patrícia
del(alunos[1]) # Remove a Maria
alunos.remove("Paulo") # Remove a primeira palavra

# ordenar uma lista
print(sorted(alunos))
alunos.sort() # ou...
print(alunos)

# indice da sentença
print(alunos.index("Pedro"))

# Inserindo em uma posição
alunos.insert(3, "João")
print(alunos)

#Contando elementos
print("Total de elementos", len(alunos))