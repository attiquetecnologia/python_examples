import pyautogui
import timeit

# url = "https://script.google.com/macros/s/AKfycbwj-oHO7mdlF8WbJMDpvL7QMkFTC0WOdI0Jjkwh76heuKlTA6wbz_9RLxDJqqZjNR_h/exec"

# pyautogui.hotkey("win", "r")
# pyautogui.write("brave " + url)
# # pyautogui.press("backspace")
# # pyautogui.press("enter")
# print(pyautogui.position())

print("Teste loop")
inicio = timeit.default_timer()
aux = 0
for p in range(1000):
    aux += p

fim = timeit.default_timer()
print("Tempo total PY", (fim-inicio))