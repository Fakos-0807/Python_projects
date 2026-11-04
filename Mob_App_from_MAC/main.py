import os
# Примусово змушуємо Kivy використовувати правильні бекенди
os.environ['KIVY_WINDOW'] = 'sdl2'
os.environ['KIVY_TEXT'] = 'sdl2'
os.environ['KIVY_IMAGE'] = 'sdl2'

from kivy.config import Config
from kivy.utils import platform

# Тимчасово прибираємо custom-позицію, щоб система сама безпечно відкрила вікно
if platform in ("win", "linux", "macosx"):
    Config.set('graphics', 'position', 'auto') 

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.properties import StringProperty
from timer import Timer
# Налаштування розміру працює стабільно
if platform in ("win", "linux", "macosx"):
    phone_height = 2340
    phone_width = 1080
    desktop_height = 1080
    scale = desktop_height / phone_height - 0.15

    Window.size = (int(phone_width * scale), int(phone_height * scale))


def check_value(value, min_value, max_value):
    try:
        value = int(value)
        if not value:
            return False
        if max_value < value or value < min_value:
            return False
        return True
    except:
        return False




class First(Screen):
    hint = StringProperty("ABC")

    def __init__(self, **kw):
        super().__init__(**kw)

    def next(self):
        app: MyApp = App.get_running_app()
        app.name = self.ids.person_name.text

        if check_value(self.ids.age.text, 7, 65) and app.name:
            app.age = int(self.ids.age.text)
            self.manager.current = 'second'
class Second(Screen):
    hint = StringProperty("Виміряйте пульс за 15 секунд.\n Результат запишіть у відповідне поле")
    def __init__(self, **kw):
        super().__init__(**kw)
        self.next_screen = False

    def timer_finished(self):
        self.ids.btn.disabled = False
        self.ids.pulse_1.disabled = False
        self.ids.btn.text = "Продовжити"
        self.next_screen = True
    
    
    def next(self):
        app: MyApp = App.get_running_app()
        if not self.next_screen:
            self.ids.btn.disabled = True
            self.ids.pulse_1.disabled = True
            self.ids.timer.start()
        else:
            if check_value(self.ids.pulse_1.text, 55, 215):
                app.pulse1 = int(self.ids.pulse_1.text)
                self.manager.current = 'third'

class Third(Screen):
    hint = StringProperty("Виконайте 30 присідань за 45 секунд.")
    def __init__(self, **kw):
        super().__init__(**kw)

    def next(self):
        self.manager.current = "four"


class Four(Screen):
    hint = StringProperty("Протягом хвилини заміряйте пульс двічі: за перші 15 секунд хвилини, а потім за останні 15 секунд. Результати запишіть у відповідні поля")    
    def __init__(self, **kw):
        super().__init__(**kw)
        self.next_screen = False

    def timer_finished(self):
            self.ids.btn.disabled = False
            self.ids.pulse_2.disabled = False
            self.ids.pulse_3.disabled = False
            self.ids.btn.text = "Продовжити"
            self.next_screen = True


    def next(self):
        app: MyApp = App.get_running_app()
        if not self.next_screen:
            self.ids.btn.disabled = True
            self.ids.pulse_2.disabled = True
            self.ids.pulse_3.disabled = True
            self.ids.timer.start()
        else:
            if check_value(self.ids.pulse_2.text, 55, 100) and check_value(self.ids.pulse_3.text, 75, 215):
                app.pulse2 = int(self.ids.pulse_2.text)
                app.pulse3 = int(self.ids.pulse_3.text)    
                self.manager.current = "five"

from calculate_index import test

class Five(Screen):    
    def __init__(self, **kw):
        super().__init__(**kw)

    def before(self):
        app:MyApp = App.get_running_app()
        self.ids.name.text = app.name
        self.ids.result.text = test(app.pulse1, app.pulse2, app.pulse3, app.age)



class MyApp(App):
    age = None
    name = None
    pulse1 = pulse2 = pulse3 = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        sm = ScreenManager()
        sm.add_widget(First(name="first"))
        sm.add_widget(Second(name="second"))
        sm.add_widget(Third(name="third"))
        sm.add_widget(Four(name="four"))
        sm.add_widget(Five(name="five"))
        
        return sm


app = MyApp()
app.run()
