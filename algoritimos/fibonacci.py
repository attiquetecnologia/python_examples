"""
O que é a sequência de Fibonacci?
A sequência de Fibonacci é uma sequência infinita de números em que cada número subsequente é a soma dos dois números anteriores. A sequência começa com 0 e 1, e a partir daí, cada número é a soma dos dois números anteriores. Portanto, a sequência começa assim: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34 e assim por diante.

Essa sequência foi criada pelo matemático italiano Leonardo Pisano, também conhecido como Fibonacci, no século XIII. A sequência de Fibonacci tem sido amplamente estudada e aplicada em várias áreas, desde matemática e ciência até arte e design.    
"""

import timeit

# Usando loops
def fibonacci(n):
    sequence = [0, 1]
    while len(sequence) < n:
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)
    return sequence

start = timeit.default_timer() # medindo eficiencia
n = 10
result = fibonacci(n)
print(result)
end = timeit.default_timer() # medindo eficiencia
print("Eficiência usando loops -> {}".format(end-start))

# Usando recursão
def fibonacci_recursive(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        sequence = fibonacci_recursive(n - 1)
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)
        return sequence

start = timeit.default_timer() # medindo eficiencia
n = 50
result = fibonacci_recursive(n)
print(result)
end = timeit.default_timer() # medindo eficiencia
print("Eficiência usando recursão -> {}".format(end-start))