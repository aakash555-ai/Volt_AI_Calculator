from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout

from widgets.display import Display
from widgets.keypad import Keypad


class HomeScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.expression = ""

        layout = BoxLayout(
            orientation="vertical",
            padding=15,
            spacing=15
        )

        self.display = Display()
        self.keypad = Keypad(button_callback=self.button_pressed)

        layout.add_widget(self.display)
        layout.add_widget(self.keypad)

        self.add_widget(layout)

    def button_pressed(self, value):

        if value == "C":
            self.expression = ""
            self.display.text = "0"
            return

        if value == "=":
            try:
                exp = self.expression.replace("×", "*").replace("÷", "/")
                result = str(eval(exp))
                self.display.text = result
                self.expression = result
            except Exception:
                self.display.text = "Error"
                self.expression = ""
            return

        if value == "AI":
            self.display.text = "AI Soon 🚀"
            return

        self.expression += value
        self.display.text = self.expression