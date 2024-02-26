from datetime import date

alunos = ["Batman", "Robin", "ScoobyDoo"]
for idx,p in enumerate(alunos):
    print(idx,p)

dia = input("dia: ")
mes = input("mes: ")
ano = input("ano: ")
niver = date(int(ano), int(mes), int(dia))
futuro = date(2049, int(mes), int(dia))
print(f"Você terá {(futuro-niver)/365}")