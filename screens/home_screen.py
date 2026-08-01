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

    def update_display(self):
        self.display.set_expression(self.expression)

        if self.expression == "":
            self.display.set_result("0")
        else:
            self.display.set_result(self.expression)

    def button_pressed(self, value):

        # ---------------- AC ----------------
        if value == "AC":
            self.expression = ""
            self.update_display()
            return

        # ---------------- DELETE ----------------
        if value == "DEL":
            self.expression = self.expression[:-1]
            self.update_display()
            return

        # ---------------- PLUS / MINUS ----------------
        if value == "±":

            if self.expression == "":
                return

            if self.expression.startswith("-"):
                self.expression = self.expression[1:]
            else:
                self.expression = "-" + self.expression

            self.update_display()
            return

        # ---------------- PERCENT ----------------
        if value == "%":

            try:
                number = float(self.expression)
                number = number / 100
                self.expression = str(number)
                self.update_display()

            except:
                self.expression = ""
                self.display.set_expression("")
                self.display.set_result("Error")

            return

        # ---------------- DECIMAL ----------------
        if value == ".":

            # Empty expression -> start with 0.
            if self.expression == "":
                self.expression = "0."
                self.update_display()
                return

            # Prevent multiple decimals in current number
            last_number = self.expression.split("+")[-1]
            last_number = last_number.split("-")[-1]
            last_number = last_number.split("×")[-1]
            last_number = last_number.split("÷")[-1]

            if "." in last_number:
                return

        # ---------------- OPERATORS ----------------
        operators = ["+", "-", "×", "÷"]

        if value in operators:

            if self.expression == "":
                return

            if self.expression[-1] in operators:
                self.expression = self.expression[:-1]

        # ---------------- EQUAL ----------------
        if value == "=":

            try:

                exp = (
                    self.expression
                    .replace("×", "*")
                    .replace("÷", "/")
                )

                result = str(eval(exp))

                self.display.set_expression(self.expression)
                self.display.set_result(result)

                self.expression = result

            except:

                self.expression = ""
                self.display.set_expression("")
                self.display.set_result("Error")

            return

        # ---------------- DEFAULT ----------------
        self.expression += value
        self.update_display()