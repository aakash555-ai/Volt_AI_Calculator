from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class DisplayPanel(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.orientation = "vertical"
        self.spacing = 10

        # Top Expression
        self.expression = Label(
            text="",
            font_size=24,
            halign="right",
            valign="middle",
            size_hint=(1, 0.35),
            color=(0.7, 0.7, 0.7, 1)
        )

        # Bottom Result
        self.result = Label(
            text="0",
            font_size=52,
            bold=True,
            halign="right",
            valign="middle",
            size_hint=(1, 0.65),
            color=(1, 1, 1, 1)
        )

        self.expression.bind(size=self.update_expression_size)
        self.result.bind(size=self.update_result_size)

        self.add_widget(self.expression)
        self.add_widget(self.result)

    def update_expression_size(self, *args):
        self.expression.text_size = (self.expression.width - 30, self.expression.height)

    def update_result_size(self, *args):
        self.result.text_size = (self.result.width - 30, self.result.height)

    def set_expression(self, text):
        self.expression.text = text

    def set_result(self, text):
        self.result.text = text