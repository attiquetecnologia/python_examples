# Classe pessoa

class Pessoa:
    nome = "Fulano"
    altura = 1.8
    peso = 68

    def imc(self):
        imc = self.peso/self.altura**2
        return imc
    
pessoa = Pessoa()
print(pessoa.imc())