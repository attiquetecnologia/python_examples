"""
Crie um programa que peça ao usuário para digitar 5 números. 
Se o usuário digitar o número 0, 
o programa deve exibir "Processamento interrompido" e sair do 
laço usando break. Caso o usuário digite os 5 números sem inserir 
nenhum zero, o programa deve exibir "Sequência processada com sucesso" 
(usando a cláusula else).
"""
# digitar 5 vezes usando range
for vez in range(5):
    digito: int = int(input("Digite um número entre 0-5: "))
    if digito == 0: 
        print("Processamento interrompido")
        break # interrompe laço
else:
    