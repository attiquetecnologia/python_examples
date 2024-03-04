import funcoes
from random_data import pessoas

def menu():
    return """
    A - Pessoas maiores de 50 anos;
    B - Pessoas que ganham mais de R$ 2000 e a porcentagem; 
        que isso representa do todo;
    C - O nome, salário, idade e profissão das 3 pessoas 
        com maiores salários;
    D - A média salarial de cada profissão;
    E - O  intervalo da maioria das idades e o sexo de quem
        ganha mais de R$ 2000. (M 39-50, F 29-30)
    --------------------------------------------------------
    Z - Sair
    """

if __name__== "__main__":
    while True:
        print(menu())
        opcao = input("Opção: ")
        if opcao == 'A':
            num = funcoes.maior_de_50(pessoas)
            print(f"\nPessoas maiores de 50 anos: {num}")
            input("\nPressiona qualquer tecla para continuar....")
        
        elif opcao == 'B':
            num = funcoes.mais_2000(pessoas)
            print(f"\nPessoas que ganham mais de R$ 2000.00: {num[0]} de {num[2]} - {num[1]}%")
            input("\nPressiona qualquer tecla para continuar....")
        
        elif opcao == 'C':
            print("Os treis maiores salários")
            pessoa = funcoes.maior_salario(pessoas)
            print(f"\n {pessoa}")
            pessoa = funcoes.maior_salario(pessoas, float(pessoa['salario']))
            print(f"\n {pessoa}")
            pessoa = funcoes.maior_salario(pessoas, float(pessoa['salario']))
            print(f"\n {pessoa}")
            
            input("\nPressiona qualquer tecla para continuar....")
        
        elif opcao == 'D':
            profissoes = funcoes.media_profissoes(pessoas) # retorna profissões
            print("Listando profissões...")
            print("Profissao", "Trabalhadores", "Média Salarial")
            for k,v in profissoes.items(): # k, é a chave principal
                print(k, v['qtd'], funcoes.formato_moeda(v['media']))

            input("\nPressiona qualquer tecla para continuar....")
        
        elif opcao == 'E':
            idades = funcoes.maior_2000_sexo(pessoas, sexo="Masculino") # retorna profissões
            print(f"\n Homens: {idades[0]} - {idades[1]} anos")
            idades = funcoes.maior_2000_sexo(pessoas, sexo="Feminino") # retorna profissões
            print(f"\n Mulheres: {idades[0]} - {idades[1]} anos")
            input("\nPressiona qualquer tecla para continuar....")
        
        elif opcao == 'Z':
            print("\nSaindo do sistema.....\n")
            break
        
        else:
            print("Você deve digitar uma opção do menu!")