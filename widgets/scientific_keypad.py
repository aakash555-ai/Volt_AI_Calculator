from kivy.uix.gridlayout import GridLayout
from widgets.calculator_button import CalculatorButton


class ScientificKeypad(GridLayout):

    def __init__(self, button_callback=None, **kwargs):
        super().__init__(**kwargs)

        self.cols = 4
        self.spacing = 10
        self.padding = 10
        self.size_hint = (1, 0.75)

        buttons = [
            "sin", "cos", "tan", "÷",
            "log", "ln", "π", "×",
            "√", "x²", "x³", "-",
            "(", ")", "^", "+",
            "ABC", "0", ".", "="
        ]

        for text in buttons:

            btn = CalculatorButton(text=text)

            if button_callback:
                btn.bind(
                    on_press=lambda instance, value=text: button_callback(value)
                )

            self.add_widget(btn)