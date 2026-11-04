from kivy.app import App
from kivy.uix.button import Button # кнопка
from kivy.uix.label import Label # напис
from kivy.uix.boxlayout import BoxLayout # макет (це теж віджет!)

class MyApp(App):
   def build(self):
      # При створенні віджету можна встановити значення його властивостей.
      # Конструктори віджетів приймають лише іменовані параметри!
      txt = Label(text='Це напис') 
      btn = Button(text='Це кнопка')
      btn2 = Button(text='Це кнопка 2')
      layout = BoxLayout(orientation='vertical', padding=40, spacing=20)
      layout.add_widget(btn2)
      layout.add_widget(btn)
      layout.add_widget(txt)
      return layout # повертається віджет, який 
                  # керує розташуванням своїх нащадків - кнопки та написи

MyApp().run()