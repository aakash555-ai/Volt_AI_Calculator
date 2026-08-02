from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout

from kivymd.uix.card import MDCard

from widgets.display_panel import DisplayPanel
from widgets.keypad import Keypad
from widgets.scientific_keypad import ScientificKeypad
from widgets.mode_switch import ModeSwitch


class HomeScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.expression = ""
        self.current_mode = "basic"

        self.layout = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=20
        )

        # ---------------- Display ----------------

        display_card = MDCard(
            radius=[30],
            elevation=4,
            padding=25,
            size_hint=(1, 0.25)
        )

        self.display = DisplayPanel()

        display_card.add_widget(self.display)

        self.layout.add_widget(display_card)

        # ---------------- Mode Switch ----------------

        self.mode_switch = ModeSwitch(
            callback=self.change_mode
        )

        self.layout.add_widget(self.mode_switch)

        # ---------------- Basic Keypad ----------------

        self.keypad = Keypad(
            button_callback=self.button_pressed
        )

        self.layout.add_widget(self.keypad)

        self.add_widget(self.layout)

        self.update_display()

    # ------------------------------------------------

    def change_mode(self, mode):

        if mode == self.current_mode:
            return

        self.layout.remove_widget(self.keypad)

        self.current_mode = mode

        if mode == "basic":

            self.keypad = Keypad(
                button_callback=self.button_pressed
            )

        else:

            self.keypad = ScientificKeypad(
                button_callback=self.button_pressed
            )

        self.layout.add_widget(self.keypad)

    # ------------------------------------------------

    def update_display(self):

        if self.expression == "":

            self.display.clear()

        else:

            self.display.set_expression(self.expression)
            self.display.set_result(self.expression)

    # ------------------------------------------------

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

    # ------------------------------------------------

    def button_pressed(self, value):

        operators = ["+", "-", "×", "÷"]

        # ---------- BASIC / SCIENTIFIC MODE BUTTONS ----------

        scientific_buttons = [
            "sin", "cos", "tan",
            "log", "ln", "π",
            "√", "x²", "x³",
            "^", "(", ")", "ABC"
        ]

        if value == "ABC":
            self.change_mode("basic")
            return

        # π
        if value == "π":
            self.expression = "3.141592653589793"
            self.update_display()
            return

        # x²
        if value == "x²":
            try:
                number = float(self.expression)
                result = number ** 2
                self.display.set_expression(f"({self.expression})²")
                self.display.set_result(str(result))
                self.expression = str(result)
            except Exception:
                self.expression = ""
                self.display.show_error()
            return

        # x³
        if value == "x³":
            try:
                number = float(self.expression)
                result = number ** 3
                self.display.set_expression(f"({self.expression})³")
                self.display.set_result(str(result))
                self.expression = str(result)
            except Exception:
                self.expression = ""
                self.display.show_error()
            return

        # √
        if value == "√":
            try:
                number = float(self.expression)

                if number < 0:
                    raise ValueError()

                result = number ** 0.5
                self.display.set_expression(f"√({self.expression})")
                self.display.set_result(str(result))
                self.expression = str(result)

            except Exception:
                self.expression = ""
                self.display.show_error()

            return

        # Remaining scientific functions
        if value in ["sin", "cos", "tan", "log", "ln", "^", "(", ")"]:
            self.display.set_result("Coming Soon")
            return

        # ---------------- AC ----------------

        if value == "AC":
            self.expression = ""
            self.display.clear()
            return

        # ---------------- DEL ----------------

        if value == "DEL":

            if self.expression:
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