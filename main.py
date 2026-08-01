from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from screens.splash_screen import SplashScreen
from screens.home_screen import HomeScreen


class VoltAICalculator(App):
    def build(self):
        sm = ScreenManager()

        sm.add_widget(SplashScreen(name="splash"))
        sm.add_widget(HomeScreen(name="home"))

        return sm


if __name__ == "__main__":
    VoltAICalculator().run()