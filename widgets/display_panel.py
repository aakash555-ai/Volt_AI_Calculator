from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class DisplayPanel(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.orientation = "vertical"
        self.spacing = 5
        self.padding = (10, 10)

        # Expression (Top)
        self.expression = Label(
            text="",
            font_size=22,
            halign="right",
            valign="middle",
            size_hint=(1, 0.35),
            color=(0.70, 0.70, 0.70, 1),
        )

        # Result (Bottom)
        self.result = Label(
            text="0",
            font_size=54,
            bold=True,
            halign="right",
            valign="middle",
            size_hint=(1, 0.65),
            color=(1, 1, 1, 1),
        )

        self.expression.bind(size=self._update_expression)
        self.result.bind(size=self._update_result)

        self.add_widget(self.expression)
        self.add_widget(self.result)

    def _update_expression(self, *args):
        self.expression.text_size = (
            self.expression.width - 20,
            self.expression.height,
        )

    def _update_result(self, *args):
        self.result.text_size = (
            self.result.width - 20,
            self.result.height,
        )

    def set_expression(self, value):
        self.expression.text = str(value)

    def set_result(self, value):
        self.result.text = str(value)

    def clear(self):
        self.expression.text = ""
        self.result.text = "0"

    def show_error(self):
        self.expression.text = ""
        self.result.text = "Error"