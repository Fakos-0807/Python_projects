# обробка події "натиснули на кнопку"

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout


class MyApp(App):
    i = 0
    def build(self):
        txt = Label(text='Це напис')
        btn = Button(text='Це кнопка')
        btn.on_press = self.test # метод on_press об'єкта btn став рівним функції tst
                            # тобто виклик btn.on_press() еквівалентний виклику tst()
                            # метод з ім'ям on_press викликається автоматично при натисканні на кнопку
                             
        layout = BoxLayout(orientation="vertical")
        layout.add_widget(txt)
        layout.add_widget(btn)
        return layout

    def test(self):
        self.i += 1
        print(self.i)

MyApp().run() # програма відстежує натискання кнопки і друкує відповідний текст.