from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock

class Timer(App):
    def build(self):
        # створення віджетів
        self.button_start = Button(
                                text="",# текст
                                font_size=25,# розмір шрифта
                                background_color = (0, 0.6, 0, 0.8),# колір фону
                                size_hint = (0.5,0.5),# розмір кнопки
                                #pos = (100,100), # позиція по координатам
                                pos_hint = {"center_x": 0.3, "center_y": 0.3},# змцщення відносно центру
                                #padding = (200,200)
                                color = (0.4,0,0.4,0.8),
                                background_normal = 'play.png',
                                background_down = 'play.png',
                                )
        self.button_stop = Button(
                                text="",
                                font_size=25,# розмір шрифта
                                background_color = (0.6, 0, 0, 0.8),# колір фону
                                size_hint = (0.5,0.5),# розмір кнопки
                                #pos = (100,100), # позиція по координатам
                                pos_hint = {"center_x": 0.3, "center_y": 0.3},# змцщення відносно центру
                                #padding = (200,200)
                                color = (0.4,0,0.4,0.8),
                                background_normal = 'pause.png',
                                background_down = 'pause.png',
                                )
        self.button_reset = Button(
                                text="",
                                font_size=25,# розмір шрифта
                                background_color = (0, 0, 0.6, 0.8),# колір фону
                                size_hint = (0.5,0.5),# розмір кнопки
                                #pos = (100,100), # позиція по координатам
                                pos_hint = {"center_x": 0.3, "center_y": 0.3},# змцщення відносно центру
                                #padding = (200,200)
                                color = (0.4,0,0.4,0.8),
                                background_normal = 'reset.jpg',
                                background_down = 'reset.jpg',
                                )
        self.text = Label(text="00:00:00")

        self.layout_v = BoxLayout(orientation="vertical")
        self.layout_h = BoxLayout()

        self.layout_h.add_widget(self.button_start)
        self.layout_h.add_widget(self.button_stop)
        self.layout_h.add_widget(self.button_reset)

        self.layout_v.add_widget(self.text)
        self.layout_v.add_widget(self.layout_h)  # Додати горизонтальний макет до вертикального макету

        self.total_seconds = 0  # кількість секунд в секундомірі
        self.running = False  # змінна, яка відповідає за активність секундоміра

        self.button_start.bind(on_press=self.start)
        self.button_stop.bind(on_press=self.stop)
        self.button_reset.bind(on_press=self.reset)

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
        self.text.text = "00:00:00"

if __name__ == '__main__':
    app = Timer()
    app.run()
