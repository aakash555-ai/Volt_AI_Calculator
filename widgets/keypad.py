from kivy.uix.gridlayout import GridLayout
from widgets.calculator_button import CalculatorButton


class Keypad(GridLayout):

    def __init__(self, button_callback=None, **kwargs):
        super().__init__(**kwargs)

        self.cols = 4
        self.spacing = 10
        self.padding = 10
        self.size_hint = (1, 0.75)

        buttons = [
            "C", "±", "%", "÷",
            "7", "8", "9", "×",
            "4", "5", "6", "-",
            "1", "2", "3", "+",
            "AI", "0", ".", "="
        ]

        for text in buttons:
            btn = CalculatorButton(text=text)

            if button_callback:
                btn.bind(on_press=lambda instance, value=text: button_callback(value))

            self.add_widget(btn)