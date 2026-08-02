from kivy.uix.boxlayout import BoxLayout

from widgets.calculator_button import CalculatorButton


class ModeSwitch(BoxLayout):

    def __init__(self, callback=None, **kwargs):
        super().__init__(**kwargs)

        self.orientation = "horizontal"
        self.spacing = 10
        self.size_hint = (1, None)
        self.height = 55

        self.basic_btn = CalculatorButton(text="Basic")
        self.scientific_btn = CalculatorButton(text="Scientific")

        if callback:
            self.basic_btn.bind(
                on_press=lambda x: callback("basic")
            )

            self.scientific_btn.bind(
                on_press=lambda x: callback("scientific")
            )

        self.add_widget(self.basic_btn)
        self.add_widget(self.scientific_btn)