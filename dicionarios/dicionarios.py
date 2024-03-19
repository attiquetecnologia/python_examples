alunos: dict = {
    1: {"nome": "Batman", "t": 9, "nota": 7}
    ,2: {"nome": "Homem Sereia", "nota": 7}
    ,3: {"nome": "Mechilãozinho", "nota": 5}
    ,4: {"nome": "Hellboy", "nota": 2}
    ,5: {"nome": "Capitão América", "nota": 5}
}
# adicionando itens
print(alunos)
alunos[6] = {"nome": "Stanislow"}
print(alunos[2]["nota"])

for chave,valor in alunos.items():
    print(alunos[chave]["nota"])