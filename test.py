from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.checkbox import CheckBox
from kivy.uix.switch import Switch
from kivy.uix.slider import Slider
from kivy.uix.spinner import Spinner
class Myapp(App):
    def build(self):
        label = Label(text='text')
        button = Button(text='press button', on_press=self.click)
        switch = Switch()
        slider = Slider()
        spinner = Spinner(text='Choice', values=('CBO','ZOV','Z','Za nashix'))
        layout = BoxLayout(orientation='horizontal',padding=30)
        layout2 = BoxLayout(orientation='vertical')
        layout3 = BoxLayout(orientation='horizontal')
        check = CheckBox()
        layout.add_widget(label)
        layout.add_widget(button)
        layout2.add_widget(check)
        layout2.add_widget(spinner)
        layout2.add_widget(slider)
        layout2.add_widget(layout)
        layout3.add_widget(layout2)
        layout3.add_widget(switch)
        return layout3
    def click(self,a):
        print('Zov')
    def swirch(self,a):
        print('CBOбода')

    pass
app = Myapp()
app.run()