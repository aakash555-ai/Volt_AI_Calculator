from kivy.uix.button import Button


class CalculatorButton(Button):

    def __init__(self, text="", **kwargs):
        super().__init__(**kwargs)

        self.text = text
        self.font_size = 24
        self.bold = True

        self.background_normal = ""

        # Default Number Button
        color = (0.20, 0.20, 0.22, 1)

        # Operator Buttons
        if text in ["÷", "×", "-", "+", "="]:
            color = (1.0, 0.58, 0.0, 1)

        # AI Button
        elif text == "AI":
            color = (0.10, 0.45, 1.0, 1)

        # Top Function Buttons
        elif text in ["C", "±", "%"]:
            color = (0.35, 0.35, 0.38, 1)

        self.background_color = color