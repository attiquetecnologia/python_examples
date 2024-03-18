# Dado um menu de opções de 0 a 5 faça um
# programa que exiba as opções pro usuário
# enquanto for diferente de 0

while True:
    print("""
    1 - opção A   
    2 - opção B
    3 - opção C
    4 - opção D
    5 - opção E
    0 - Sair
    """)
    opcao: str = input("Opção: ")
    if opcao == '0':
        break