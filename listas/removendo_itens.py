carros = ['Vectra', 'Astra', 'Palio', 'Saveiro', 'Masserati']

#contar itens primeiro
count = len(carros)

#Loop for para exibir itens com range(count)
for idx in range(count):
    print(idx, carros[idx])

apagar = int(input("Apague um: "))
del carros[apagar]

for idx in range(count):
    print(idx, carros[idx])