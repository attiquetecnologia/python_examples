import itertools

def gerar_tabela_verdade(expressao_str, nomes_variaveis):
    """
    Gera e exibe a tabela-verdade para uma expressão lógica.
    expressao_str: String com a expressão Python (ex: 'not (A and B)')
    nomes_variaveis: Lista com os nomes das variáveis (ex: ['A', 'B'])
    """
    # Cabeçalho da tabela
    cabecalho = " | ".join(nomes_variaveis) + f" | Resultado: {expressao_str}"
    print(cabecalho)
    print("-" * len(cabecalho))
    
    # Gera todas as combinações de True/False para as variáveis
    combinações = list(itertools.product([True, False], repeat=len(nomes_variaveis)))
    
    for comb in combinações:
        # Mapeia cada variável para seu valor na combinação atual
        contexto = dict(zip(nomes_variaveis, comb))
        
        # Avalia a expressão no contexto das variáveis
        resultado = eval(expressao_str, {}, contexto)
        
        # Formata a exibição das entradas e do resultado
        linha_vars = " | ".join(f"{str(val):5}" for val in comb)
        print(f"{linha_vars} | {str(resultado)}")

# --- Exemplo de Uso ---
# Testando a fbf: (A or B) and not (A and B) [Ou Exclusivo / XOR]
variaveis = ['A', 'B']
expressao = "(A or B) and not (A and B)"

print("=== AVALIADOR DE EXPRESSÕES BOOLEANAS ===")
gerar_tabela_verdade(expressao, variaveis)