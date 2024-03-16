import timeit

# É possível concluir que o uso de Type Hints (anotações de tipo) não deixam o código
# mais eficiente ao contrário há uma ligeira perda que em calculos mais complexos pode
# gerar mais frustração
# A vantagem do type hint como diz na documentação é para IDEs, documentação (no caso a docstrings
# muito mais eficiente do que isso), para alunos em fase de aprendizagem (eu penso que os simbolos
# farão mais confusão na cabeça do aluno), para fazer testes com mypy e desenvolvedores de outras
# linguagens de tipagem estática

eficiencia = timeit.timeit('a: str = "abelha"', number=10) # medindo eficiencia
print("Eficiência com tipo primitivo a: str -> {}".format(eficiencia))

eficiencia = timeit.timeit('a = "abelha"', number=10) # medindo eficiencia
print("Eficiência sem tipo primitivo a -> {}".format(eficiencia))

eficiencia = timeit.timeit('a: int = 10', number=10) # medindo eficiencia
print("Eficiência com tipo primitivo a: int -> {}".format(eficiencia))

eficiencia = timeit.timeit('a = 10', number=10) # medindo eficiencia
print("Eficiência sem tipo primitivo a -> {}".format(eficiencia))

print("Testando funções!")
def soma_A(a: int, b: int) -> int:
    return a + b
eficiencia = timeit.timeit("soma_A(10, 9)", "from __main__ import soma_A", number=10) # medindo eficiencia
print("Eficiência com tipo primitivo-> {}".format(eficiencia))


print("Testando funções!")
def soma_B(a, b):
    return a + b
eficiencia = timeit.timeit("soma_B(10, 9)", "from __main__ import soma_B", number=10) # medindo eficiencia
print("Eficiência sem tipo primitivo-> {}".format(eficiencia))