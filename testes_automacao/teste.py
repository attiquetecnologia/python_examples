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

fim = timeit.timeit("incremento()", "from __main__ import incremento", number=10)
print("Tempo total incremento Python -> {}".format(fim))

def loop():
    i = 1
    for i in iter(range(1000000000)):
        pass
fim = timeit.timeit("loop()", "from __main__ import loop", number=10)
print("Tempo total loop até 1bi PY -> {}".format(fim))

# O mesmo exemplo acima com numpy
# def loop():
#     import numpy as np
#     i = 1
#     for i in np.arange(1000000000):
#         pass
# fim = timeit.timeit("loop()", "from __main__ import loop", number=2)
# print("Tempo total loop até 1bi PY -> {}".format(fim))

# Usando list compression
# def loop():
    
#     i = (i for i in range(1000000000))
# fim = timeit.timeit("loop()", "from __main__ import loop", number=2)
# print("Tempo total loop até 1bi PY -> {}".format(fim))