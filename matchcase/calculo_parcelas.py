print('--- Bem-vindo à Calculadora de Parcelas! ---')

PARCELAS_SEM_JUROS_MAX = 6 # Define o máximo de parcelas sem juros

preco = 120.0 #precço do produto, tenis
DESCONTO = 0.05
JUROS_MES = 0.02

print('--- ESCOLHA UMA FORMA DE PAGAMENTO ---\n1 - A Vista\n2 - Parcelado')
forma_pgto = input("Resposta: ")
print("Forma de pagamento escolhida:", forma_pgto)
match forma_pgto:
    case "1":
        desconto = preco * DESCONTO
        preco = preco - desconto
        print("Preço a vista:", preco)
        
    case "2":
        n_parcelas = input("Parcele em até 6x sem juros: ")
        n_parcelas = int(n_parcelas) #converte para inteiro
        if n_parcelas<=6:
            for p in range(n_parcelas):
                print(f"Parcela s/juros {p} -> R$ {preco/n_parcelas}")
            
        else:
            for p in range(n_parcelas):
                juros = preco*n_parcelas*JUROS_MES
                print(f"Parcela c/juros {p} -> R$ {preco/n_parcelas+juros}")
    case _: # _ representa o default
        print("Escolha uma opção do menu.")

# fim match
# totalCompra = parseFloat(totalCompraStr.replace(',', '.')) # Garante que seja float e aceita vírgula