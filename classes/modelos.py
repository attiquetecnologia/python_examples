"""
Modelos de classe
"""

class Aluno:
    nome = "Batolomeu"
    idade = 10

    def __init__(self):
        self.peso = 120.0
        self.altura = 1.60

    def imc(self):
        return self.peso/self.altura**2
    
    def __str__(self):
        return f"Aluno: {self.nome}\nIdade: {self.idade}"
    

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f"Nome:{self.nome}\nPreço:{self.preco}"

class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def __str__(self):
        return f"Marca:{self.marca}\nModelo:{self.modelo}\nAno: {self.ano}"

