# Gerador de Tabela-Verdade
print(" A | B | A AND B | A OR B | A -> B ")
print("-" * 35)

for A in [True, False]:
    for B in [True, False]:
        and_res = A and B
        or_res = A or B
        cond_res = (not A) or B
        print(f"{str(A):5} | {str(B):5} | {str(and_res):7} | {str(or_res):6} | {str(cond_res):6}")