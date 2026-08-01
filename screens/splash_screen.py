from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.clock import Clock


class SplashScreen(Screen):

    def on_enter(self):
        Clock.schedule_once(self.go_home, 2)

    def go_home(self, dt):
        self.manager.current = "home"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.add_widget(
            Label(
                text="⚡\nVolt AI Calculator",
                font_size=32,
                halign="center"
            )
        )