# Uma lanchonete oferece 3 opções de lanche e 2 opções de bebidas

lanches = ['Hotdog', 'Pastel', 'Hamburger']
bebidas = ['Suco', 'Refrigerante']

op: int = 1 # contador
for l in lanches:
    for b in bebidas:
        print(f"Opção {op} => {l} + {b}")
        op += 1