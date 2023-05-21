from kivy.config import Config
from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.progressbar import ProgressBar
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.uix.image import Image
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window
from kivy.uix.button import Button


class SplashScreen(Screen):
    def __init__(self, **kwargs):
        super(SplashScreen, self).__init__(**kwargs)

        # Set background color
        with self.canvas.before:
            Color('white')  # Set white color
            self.rect = Rectangle(size=(1024, 600), pos=self.pos)

        # Add logo image
        self.add_widget(Image(source='images\logos\logo_small.png', size_hint=(0.5, 0.5),
                              pos_hint={'center_x': 0.5, 'center_y': 0.6},
                              allow_stretch=True, keep_ratio=True))

        # Add progress bar
        self.progress_bar = ProgressBar(max=10, size_hint=(0.8, 0.1),
                                        pos_hint={'center_x': 0.5, 'center_y': 0.25})
        self.add_widget(self.progress_bar)

        # Add message label
        self.message_label = Label(text='Powering UP', size_hint=(0.8, 0.1),
                                   pos_hint={'center_x': 0.5, 'center_y': 0.15},
                                   font_size=24, color='black')
        self.add_widget(self.message_label)

        # Start the progress bar animation
        Clock.schedule_interval(self.update_progress, 1)  # Update every second

    def update_progress(self, dt):
        progress = self.progress_bar.value + 1
        self.progress_bar.value = progress

        if progress == 1:
            self.message_label.text = 'Sending Information to Skynet Host'
        elif progress == 3:
            self.message_label.text = 'Initiation Permission Granted'
        elif progress == 4:
            self.message_label.text = 'Security Protocols Engaged'
        elif progress == 5:
            self.message_label.text = 'AP - Mines Armed'
        elif progress == 6:
            self.message_label.text = 'Sentinel Drones Dispatched'
        elif progress == 7:
            self.message_label.text = 'Perimeter Defense Established'
        elif progress == 8:
            self.message_label.text = 'User Signatures Registered'
        elif progress == 9:
            self.message_label.text = 'FOF System ACTIVE'
        elif progress == 10:
            self.message_label.text = 'Loading complete'
            Clock.schedule_once(lambda dt: self.switch_to_main_app(), 1)

    def switch_to_main_app(self):
        app = App.get_running_app()
        app.root.current = 'main'


class MyRelativeLayout(Screen):
    def __init__(self, **kwargs):
        super(MyRelativeLayout, self).__init__(**kwargs)

        # Set background image
        self.add_widget(Image(source='images\gui\\backgroud_base.png', allow_stretch=True, keep_ratio=False))

        # Create the three buttons
        self.create_buttons()

    def create_buttons(self):
        # Create the buttons
        button1 = Button(text='Steuerung', size_hint=(None, None), size=(300, 300),
                     pos_hint={'x': 0.025, 'y': 0.25}, font_size=36, color=(0, 0, 0, 1))
        button2 = Button(text='Sicherheit', size_hint=(None, None), size=(300, 300),
                     pos_hint={'x': 0.35, 'y': 0.25}, font_size=36, color=(0, 0, 0, 1))
        button3 = Button(text='Gesundheit', size_hint=(None, None), size=(300, 300),
                     pos_hint={'x': 0.675, 'y': 0.25}, font_size=36, color=(0, 0, 0, 1))

        # Set the button images #TODO add button_down effect
        button1.background_normal = 'images\gui\large_button.png'
        button2.background_normal = 'images\gui\large_button.png'
        button3.background_normal = 'images\gui\large_button.png'

        # Add the buttons to the screen
        self.add_widget(button1)
        self.add_widget(button2)
        self.add_widget(button3)


class MyApp(App):
    def build(self):
        screen_manager = ScreenManager()

        # Add the splash screen
        splash_screen = SplashScreen(name='splash')
        screen_manager.add_widget(splash_screen)

        # Add the main screen
        main_screen = MyRelativeLayout(name='main')
        screen_manager.add_widget(main_screen)

        return screen_manager


if __name__ == '__main__':
    MyApp().run()
