from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class Tempate_Button(Button):
    def __init__(self, screen, direction='right', goal='main', **kwargs):
        super().__init__(**kwargs) # запускаємо конструктор класу Button
        self.screen = screen
        self.direction = direction
        self.goal = goal
    def on_press(self): # при натисканні напрямок, екран для зміни
        self.screen.manager.transition.direction = self.direction
        self.screen.manager.current = self.goal

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        button = Tempate_Button(self, direction='left', goal='main2', text='1')
        button2 = Tempate_Button(self, direction='right', goal='main3', text='second screen')
        label = Label(text='Натисни на кнопку')
        layout = BoxLayout()
        layout.add_widget(button2)
        layout.add_widget(button)
        self.add_widget(layout)
class Second_screen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        button3 = Tempate_Button(self, direction='right', goal='main', text='back')
        layout = BoxLayout()
        layout.add_widget(button3)
        self.add_widget(layout)

class Third_screen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        button3 = Tempate_Button(self, direction='left', goal='main', text='back')
        self.add_widget(button3)

class MyApp(App):
    def build(self):
        manager = ScreenManager()
        manager.add_widget(MainScreen(name='main'))
        manager.add_widget(Second_screen(name='main2'))
        manager.add_widget(Third_screen(name='main3'))

        return manager

if __name__ == '__main__':
    app = MyApp()
    app.run()