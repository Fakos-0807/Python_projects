from kivy.app import App 
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.utils import platform
from kivy.core.window import Window
from kivy.properties import StringProperty


if platform in ("win", "linux", "macosx"):
    phone_height = 2340
    phone_width = 1080
    desktop_height = 1080
    scale = desktop_height/phone_height -0.15

    Window.size = (int(phone_width * scale), int(phone_height * scale))
    Window.top = 50
    Window.left = 120


class First(Screen):
    hint = StringProperty("ÄBC")
    def __init__(self, **kw):
        super().__init__(**kw)    


    def next(self):
        print("Second screen here ->")

class Second(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)


    def next(self):
        pass

class MyApp(App):
    age = None
    name = None
    pulse1 = pulse2 = pulse3 = None
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        sm = ScreenManager()
        sm.add_widget(First(name = "first"))
        sm.add_widget(Second(name = "second"))
        return sm