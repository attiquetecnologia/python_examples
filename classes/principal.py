from modelos import Aluno, Produto, Carro

if __name__ == "__main__":
    a1 = Aluno()
    print(a1.nome, a1.idade)
    print(Aluno.nome)
    # print(Aluno.peso) erro
    print(Aluno().peso)
    a1.nome = "Bartolomeu Simpson"
    print(a1.nome)
    Aluno.nome = "Faia"
    print(Aluno.nome)
    print(a1.nome, a1.imc())
    print(a1, Aluno)
    print(100*"-")
    print("Exbir produto")
    print(Produto("Monjaro", 800))
    print(Produto("Simancol", 100))
    print(Produto("Supositório Zagalo", 800))

    fusca = Carro("VolksWagen", "Sedan", 1994)
    peugeot206 = Carro("Peugeot", "206", 2006)
    marea = Carro("FIAT", "Marea", 2001)

    print(20*"-")