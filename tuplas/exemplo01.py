# Tuplas são imutáveis, ou seja, não podem ser alteradas depois de criadas.

vazio = ()
unitário = 'olá', # <!- note a vírgula ao final
print(len(vazio))
print(len(unitário))
print(unitário)

t = 12345, 54321, 'bom dia!'

x, y, z = t # desempacotamento de sequência
print(x, y, z) # requer que haja tantas variáveis no lado esquerdo do sinal de igual