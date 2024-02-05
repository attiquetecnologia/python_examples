#programa média
nome_do_aluno = input("Seu nome: ")
p1 = float(input("P1: "))
p2 = float(input("P2: "))
t = float(input("T: "))
media = p1*0.35+p2*0.35+t*0.3
print(f"Olá, {nome_do_aluno} sua média final é {media}.")
if media>5:
    print(f"Parabéns, {nome_do_aluno}, você foi aprovado!")
else:
    print(f"Infelizmente, {nome_do_aluno}, você foi reprovado!")