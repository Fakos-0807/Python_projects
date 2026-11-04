from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.properties import BooleanProperty, NumericProperty

class Timer(Label):
    done = BooleanProperty(False)
    current_time = NumericProperty(0)
    total_time = NumericProperty(0)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text = f"Пройшло секунд: {self.current_time}"

    def start(self):
        self.event = Clock.schedule_interval(self.update, 1)

    def restart(self, total):
        self.done = False
        self.current_time = 0
        self.total_time = total
        self.start()

    def update(self, dt):
        if self.current_time < self.total_time:
            self.current_time += 1
            self.text = f"Пройшло секунд: {self.current_time}"
        else:
            self.done = True
            return False
        