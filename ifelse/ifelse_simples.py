# Faça um programa que dado 2 números exiba
# para o usuário qual é o maior número.
# Nota: if sempre testa variáveis.

numero1: int = 10 # número inteiro
numero2: int = 11 # número inteiro
if numero1 > numero2:
    print(f"O número {numero1} é o maior.")
else:
    print(f"O número {numero2} é o maior.")

# 2) Dado a venda de um produto calcule a comissão
# conforme a tabela abaixo.
# Se venda > 100000 (cem mil) comissão 5%
# senão se venda > 50000 (cinquenta mil) comissão 7%
# senão comissão 10%

venda: float = float(input("Valor venda: "))
if venda > 10000:
    print(f"Comissão: {venda*0.05}")
elif venda > 50000:
    print(f"Comissão: {venda*0.07}")
else:
    print(f"Comissão: {venda*0.10}")