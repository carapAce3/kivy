from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager, Screen

class Timer(App):
    def build(self):
        #створення вiджетiв
        self.button_start = Button(text='START', on_press=self.start)
        self.button_stop = Button(text='STOP', on_press=self.stop)
        self.button_reset = Button(text='RESET')
        self.text = Label(text='00:00:00')

        self.layout_v = BoxLayout(orientation='vertical')
        self.layout_h = BoxLayout()

        self.layout_h.add_widget(self.button_start)
        self.layout_h.add_widget(self.button_stop)
        self.layout_h.add_widget(self.button_reset)

        self.layout_v.add_widget(self.text)
        self.layout_v.add_widget(self.layout_h)
        
        self.total_seconds = 0
        self.running = False

        return self.layout_v
    
    def update_time(self, instance):
        self.total_seconds += 1
        hour, ostacha = divmod(self.total_seconds, 3600)
        minute, second = divmod(ostacha, 60)
        self.text.text = f"{hour:02}:{minute:02}:{second:02}"

    def start(self, instance):
        if not self.running:
            self.running = True
            Clock.schedule_interval(self.update_time, 1)
    def stop(self, instance):
        if self.running:
            self.running = False
            Clock.unschedule(self.update_time)
    def reset(self, instance):
        self.stop(instance)
        self.total_seconds = 0
        self.text.text = '00:00:00'




if __name__ == '__main__':
    app = Timer()
    app.run()