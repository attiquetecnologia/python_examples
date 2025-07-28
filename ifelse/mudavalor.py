#Algorítmo troca de valores

a: int = 10
b: int = 2
if a %2 == 0: # é par?
    a = b * a # altera valor de a
print(f"a: {a} e b: {b}")

# >>> a: 20 e b: 2

while b < 100:
    b = b + a # altera o valor de b
    print(f"a: {a} e b: {b}")
    # >>> a: 20 e b: ???

b = a - 4 # altera o valor de a
print(f"a: {a} e b: {b}")
# >>> a: 16 e b: 22

