import tkinter as tk

class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

        self.entrythingy = tk.Entry()
        self.entrythingy.pack()

        # Cria a variável da aplicação.
        self.contents = tk.StringVar()
        # Define-a com algum valor.
        self.contents.set("this is a variable")
        # Fala para o widget de entrada para monitorar essa variável.
        self.entrythingy["textvariable"] = self.contents

        # Define um retorno de chamada para quando o usuário pressionar Enter.
        # Isso imprime o valor atual da variável.
        self.entrythingy.bind('<Key-Return>',
                             self.print_contents)

    def print_contents(self, event):
        print("Hi. The current entry content is:",
              self.contents.get())

root = tk.Tk()
myapp = App(root)
myapp.mainloop()