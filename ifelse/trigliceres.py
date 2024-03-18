j: str = input("Você está em jejum s/n? ")
t: str = input("Trigliceres? ")
t: int = int(t) # converter pra int
if j == 's':
    if t > 150:
        print("Está alto!")
    else:
        print("Está normal!")
else:
    if t > 175:
        print("Está alto!")
    else:
        print("Está normal!")