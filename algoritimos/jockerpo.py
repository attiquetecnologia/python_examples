# Jocker Po - Pedra, Papel,Tesoura
# Jogo para dois jogadores sem interação com usuário
# Pedra > Tesoura > Papel > Pedra
# Se Jogador1: Papel e Jogador2: Pedra, Jogador1
# Uso da função random do python

# O grande problema do algorítimo é arranjar uma forma inteligente de jogar e permitir que 
# outros jogadores entrem no jogo da forma escolhida isso não é possível.

# Começar pela jogada, prototipo
import random
from enum import Enum

class Escolha(Enum):
    PEDRA = 0
    PAPEL = 1
    TESOURA = 2

class Jogador:
    def __init__(self, nome: str):
        self.nome: str = nome
        # Escolhe na instancia
        self.escolha: Escolha = Escolha(random.randrange(0,2))

    def __str__(self):
        return f"Jogador {self.nome}, escolheu: {self.escolha}"

class Jogada:
    def __init__(self, jogador_a: Jogador, jogador_b: Jogador):
        self.jogador_a: Jogador = jogador_a
        self.jogador_b: Jogador = jogador_b
        self.comparar()

    def comparar(self) -> str:
        print(self.jogador_a, self.jogador_b)
        if self.jogador_a.escolha == Escolha.PEDRA and self.jogador_b.escolha  == Escolha.TESOURA:
            print("Jogador A venceu")
        elif self.jogador_a.escolha == Escolha.TESOURA and self.jogador_b.escolha  == Escolha.PAPEL:
            print("Jogador A venceu")
        elif self.jogador_a.escolha == Escolha.PAPEL and self.jogador_b.escolha  == Escolha.PEDRA:
            print("Jogador A venceu")
        else:
            print("EMPATE")

if __name__ == "__main__":
    for p in range(3):
        Jogada(Jogador("Rodrigo"), Jogador("Felipe"))