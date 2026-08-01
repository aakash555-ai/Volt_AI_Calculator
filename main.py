from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager

from screens.splash_screen import SplashScreen
from screens.home_screen import HomeScreen


class VoltAICalculator(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"

        sm = ScreenManager()

        sm.add_widget(SplashScreen(name="splash"))
        sm.add_widget(HomeScreen(name="home"))

        return sm


if __name__ == "__main__":
    VoltAICalculator().run()