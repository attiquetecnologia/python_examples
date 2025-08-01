from kivy.app import App
from kivy.uix.widget import Widget

class Tela(Widget):
    pass

class CadastroApp(App):
    def build(self):
        app = Tela()
        return app


if __name__ == '__main__':
    CadastroApp().run()