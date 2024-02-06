# Nome, Média
notas = {
    1: ("Batman", 10)
    ,2: ("Coringa", 10)
    ,3: ("Robin", 7)
}

for k,v in list(notas.items()):
    print(sum(v[1:3])/len(v[1:3]))
    