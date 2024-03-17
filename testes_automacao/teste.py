# import pyautogui
import timeit

# url = "https://script.google.com/macros/s/AKfycbwj-oHO7mdlF8WbJMDpvL7QMkFTC0WOdI0Jjkwh76heuKlTA6wbz_9RLxDJqqZjNR_h/exec"

# pyautogui.hotkey("win", "r")
# pyautogui.write("brave " + url)
# # pyautogui.press("backspace")
# # pyautogui.press("enter")
# print(pyautogui.position())

print("Teste loop")

def incremento() -> int:
    aux: int = 0
    for p in range(1000):
        aux += p
    return aux

# fim = timeit.timeit("incremento()", "from __main__ import incremento", number=10)
# print("Tempo total incremento Python -> {}".format(fim))
# >>> Tempo total incremento Python -> 0.000851409999995667
# Rodando com baitecode .pyc
# >>> Tempo total incremento Python -> 0.00021341599995139404
# Usando pypy
# >>> Tempo total incremento Python -> 0.01028917899998305

# Esse loop pode facilmente obter melhores resultados usando o pypy
# def loop():
#     i = 1
#     for i in iter(range(1000000000)):
#         pass
# fim = timeit.timeit("loop()", "from __main__ import loop", number=10)
# print("Tempo total loop até 1bi PY -> {}".format(fim))
# Rodando diretamente o .py pode chegar a mais de 1 minuto
# Rodando bytecode .pyc
# >>> Tempo total loop até 1bi PY -> 109.54372049599988
# Usando pypy
# >>> Tempo total loop até 1bi PY -> 5.325492441000051

# O mesmo exemplo acima com numpy
# def loop():
#     import numpy as np
#     i = 1
#     for i in np.arange(1000000000):
#         pass
# fim = timeit.timeit("loop()", "from __main__ import loop", number=10)
# print("Tempo total loop até 1bi PY -> {}".format(fim))
# Rodando diretamente o .py 
# >>> Tempo total loop até 1bi PY -> 546.0413083239998
# Rodando bytecode .pyc
# >>> Tempo total loop até 1bi PY -> 246.61347042299985
# Usando pypy
# >>> por algum motivo o processo está Morto


# Usando list compression
# def loop():
#     i = (i for i in range(1000000000))
# fim = timeit.timeit("loop()", "from __main__ import loop", number=2)
# print("Tempo total loop até 1bi PY -> {}".format(fim))
# Rodando diretamente o .py 
# >>> Tempo total loop até 1bi PY -> 0.00011350999920978211
# Rodando bytecode .pyc
# >>> Tempo total loop até 1bi PY -> 3.4570002753753215e-06
# Usando pypy
# >>> Tempo total loop até 1bi PY -> 7.0750002123531885e-06

# Usando NUMBA
from numba import njit

@njit
def loop():
    for i in iter(range(1000000000)):
        pass
fim = timeit.timeit("loop()", "from __main__ import loop", number=10)
print("Tempo total loop até 1bi PY -> {}".format(fim))
# Rodando diretamente o .py 
# >>> Tempo total loop até 1bi PY -> 0.25235420699937094
# Rodando bytecode .pyc
# >>> Tempo total loop até 1bi PY -> 0.0911239340002794
# Usando pypy
# >>> não existe numba pro pypy

# CONCLUSÕES
#   Até o momento posso concluir que existe diferenças em alguns algoritimos usando 
# as técnicas porém não é um concenso, é possível ver que o pypy é rápido para alguns casos
# mas possui limitações de bibliotecas.
#   A otimização usando list compression foi surpreendente, além é claro do uso do bytecode.