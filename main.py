from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
class myapp(GridLayout):
    def __init__(self, **kwargs):
        super(myapp, self).__init__(**kwargs)
        self.cols = 2

        self.add_widget(Label(text='Usuario'))
        self.usuario = TextInput(multiline=True)
        self.add_widget(self.usuario)

        self.add_widget(Label(text='Senha'))
        self.senha = TextInput(password=True, multiline=False)
        self.add_widget(self.senha)

class runapp(App):
    def build(self):
        return myapp()

runapp().run()