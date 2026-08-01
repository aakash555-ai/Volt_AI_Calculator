from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout

from kivymd.uix.card import MDCard

from widgets.display_panel import DisplayPanel
from widgets.keypad import Keypad


class HomeScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.expression = ""

        layout = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=20
        )

        display_card = MDCard(
            radius=[30],
            elevation=4,
            padding=25,
            size_hint=(1, 0.25)
        )

        self.display = DisplayPanel()
        display_card.add_widget(self.display)

        self.keypad = Keypad(button_callback=self.button_pressed)

        layout.add_widget(display_card)
        layout.add_widget(self.keypad)

        self.add_widget(layout)

        self.update_display()

    def update_display(self):

        if self.expression == "":
            self.display.clear()
        else:
            self.display.set_expression(self.expression)
            self.display.set_result(self.expression)

    def calculate_result(self):

        try:
            exp = (
                self.expression
                .replace("×", "*")
                .replace("÷", "/")
            )

            return str(eval(exp))

        except Exception:
            return None

    def button_pressed(self, value):

        operators = ["+", "-", "×", "÷"]

        # ---------------- AC ----------------

        if value == "AC":
            self.expression = ""
            self.display.clear()
            return

        # ---------------- DEL ----------------

        if value == "DEL":

            self.expression = self.expression[:-1]
            self.update_display()
            return

        # ---------------- ± ----------------

        if value == "±":

            if self.expression == "":
                return

            if self.expression.startswith("-"):
                self.expression = self.expression[1:]
            else:
                self.expression = "-" + self.expression

            self.update_display()
            return

        # ---------------- % ----------------

        if value == "%":

            try:
                number = float(self.expression)
                number = number / 100
                self.expression = str(number)
                self.update_display()

            except Exception:
                self.expression = ""
                self.display.show_error()

            return

        # ---------------- Decimal ----------------

        if value == ".":

            if self.expression == "":
                self.expression = "0."
                self.update_display()
                return

            last = self.expression

            for op in operators:
                last = last.split(op)[-1]

            if "." in last:
                return

        # ---------------- Operators ----------------

        if value in operators:

            if self.expression == "":
                return

            if self.expression[-1] in operators:
                self.expression = self.expression[:-1]

        # ---------------- Equal ----------------

        if value == "=":

            result = self.calculate_result()

            if result is None:
                self.expression = ""
                self.display.show_error()
            else:
                self.display.set_expression(self.expression)
                self.display.set_result(result)
                self.expression = result

            return

        # ---------------- Default ----------------

        self.expression += value
        self.update_display()