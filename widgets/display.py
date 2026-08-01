from kivy.uix.label import Label


class Display(Label):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.text = "0"

        self.font_size = 52

        self.bold = True

        self.halign = "right"

        self.valign = "middle"

        self.size_hint = (1, 0.25)

        self.bind(size=self.update_text_size)

    def update_text_size(self, *args):
        self.text_size = self.size