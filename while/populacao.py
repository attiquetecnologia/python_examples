ano=0
popA = 8000
taxaA = 0.03
taxaB = 0.015
popB = 200000
while popA < popB:
    ano += 1
    popA = int((1 + (taxaA/100) )* popA)
    popB = int((1 + (taxaB/100) )* popB)
    print("Ano %d:" % ano)
    print("Populaçao A: %d" % popA)
    print("População B: %d\n\n" % popB)

print("Ultrapassa no ano:",ano)