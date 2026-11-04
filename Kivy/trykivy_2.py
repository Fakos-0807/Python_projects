# додаток з одним віджетом.

from kivy.app import App
# всі віджети знаходяться в окремих модулях усередині kivy.uix:
from kivy.uix.button import Button # кнопка
from kivy.uix.label import Label # текстовий напис

class MyApp(App):
   # якщо в об'єкті класу App є метод build(),
   # run() виконає цей метод
   # і виведе на екран те, що повертає build
   def build(self):
      btn = Button(text='Це кнопка')
      txt = Label(text = 'Напис на екрані', color = 'red')
      return txt # повертається завжди віджет!

app = MyApp()
app.run() # буде показано віджет класу Button