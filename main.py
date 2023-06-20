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
from kivy.uix.slider import Slider
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

import os


class SplashScreen(Screen):
    def __init__(self, **kwargs):
        super(SplashScreen, self).__init__(**kwargs)

        with self.canvas.before:
            Color("white")
            self.rect = Rectangle(size=(1024, 600), pos=self.pos)

        self.add_widget(
            Image(
                source="Images/logos/logo_small.png",
                size_hint=(0.5, 0.5),
                pos_hint={"center_x": 0.5, "center_y": 0.6},
                allow_stretch=True,
                keep_ratio=True,
            )
        )

        self.progress_bar = ProgressBar(
            max=10, size_hint=(0.8, 0.1), pos_hint={"center_x": 0.5, "center_y": 0.25}
        )
        self.add_widget(self.progress_bar)

        self.message_label = Label(
            text="Powering UP",
            size_hint=(0.8, 0.1),
            pos_hint={"center_x": 0.5, "center_y": 0.15},
            font_size=24,
            color="black",
        )
        self.add_widget(self.message_label)

        Clock.schedule_interval(self.update_progress, 1)

    def update_progress(self, dt):
        progress = self.progress_bar.value + 1
        self.progress_bar.value = progress

        if progress == 1:
            self.message_label.text = "Sending Information to Skynet Host"
        elif progress == 3:
            self.message_label.text = "Initiation Permission Granted"
        elif progress == 4:
            self.message_label.text = "Security Protocols Engaged"
        elif progress == 5:
            self.message_label.text = "AP - Mines Armed"
        elif progress == 6:
            self.message_label.text = "Sentinel Drones Dispatched"
        elif progress == 7:
            self.message_label.text = "Perimeter Defense Established"
        elif progress == 8:
            self.message_label.text = "User Signatures Registered"
        elif progress == 9:
            self.message_label.text = "FOF System ACTIVE"
        elif progress == 10:
            self.message_label.text = "Loading complete"
            Clock.schedule_once(lambda dt: self.switch_to_main_app(), 1)

    def switch_to_main_app(self):
        app = App.get_running_app()
        app.root.current = "main"


class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)

        self.add_widget(
            Image(
                source="Images/gui/backgroud_base.png",
                allow_stretch=True,
                keep_ratio=False,
            )
        )

        self.create_buttons()

    def create_buttons(self):
        button_steuerung = Button(
            text="Steuerung",
            size_hint=(None, None),
            size=(300, 300),
            pos_hint={"x": 0.025, "y": 0.25},
            font_size=36,
            color=(0, 0, 0, 1),
        )
        button_sicherheit = Button(
            text="Sicherheit",
            size_hint=(None, None),
            size=(300, 300),
            pos_hint={"x": 0.35, "y": 0.25},
            font_size=36,
            color=(0, 0, 0, 1),
        )
        button_gesundheit = Button(
            text="Gesundheit",
            size_hint=(None, None),
            size=(300, 300),
            pos_hint={"x": 0.675, "y": 0.25},
            font_size=36,
            color=(0, 0, 0, 1),
        )

        button_profil = Button(
            text="",
            size_hint=(None, None),
            size=(50, 50),
            pos_hint={"x": 0.93, "y": 0.88},
        )
        button_settings = Button(
            text="",
            size_hint=(None, None),
            size=(50, 50),
            pos_hint={"x": 0.87, "y": 0.88},
        )

        button_steuerung.background_normal = "Images/gui/large_button.png"
        button_steuerung.background_down = "Images/gui/large_button_pressed.png"
        button_sicherheit.background_normal = "Images/gui/large_button.png"
        button_sicherheit.background_down = "Images/gui/large_button_pressed.png"
        button_gesundheit.background_normal = "Images/gui/large_button.png"
        button_gesundheit.background_down = "Images/gui/large_button_pressed.png"
        button_profil.background_normal = "Images/symbols/benutzer_tiny.png"
        button_profil.background_down = "Images/symbols/benutzer_tiny_pressed.png"
        button_settings.background_normal = "Images/symbols/einstellungen_tiny.png"
        button_settings.background_down = (
            "Images/symbols/einstellungen_tiny_pressed.png"
        )

        self.add_widget(button_steuerung)
        self.add_widget(button_sicherheit)
        self.add_widget(button_gesundheit)
        self.add_widget(button_profil)
        self.add_widget(button_settings)

        button_settings.bind(on_release=self.open_settings_screen)
        button_steuerung.bind(on_release=self.open_control_screen)
        button_profil.bind(on_release=self.open_profile_screen)
        button_sicherheit.bind(on_release=self.show_popup_notimplemented)
        button_gesundheit.bind(on_release=self.show_popup_notimplemented)

    def open_settings_screen(self, instance):
        app = App.get_running_app()
        app.root.current = "settings"

    def open_control_screen(self, instance):
        app = App.get_running_app()
        app.root.current = "control"

    def open_profile_screen(self, instance):
        app = App.get_running_app()
        app.root.current = "profile"

    def show_popup_notimplemented(self, instance):
        content = BoxLayout(orientation="vertical")
        label = Label(text="This Feature is not yet implemented", font_size=24)
        content.add_widget(label)

        popup = Popup(
            title="Information",
            content=content,
            size_hint=(None, None),
            size=(400, 400),
        )
        popup.open()


class SettingsScreen(Screen):
    def __init__(self, **kwargs):
        super(SettingsScreen, self).__init__(**kwargs)

        self.add_widget(
            Image(
                source="Images/gui/backgroud_base.png",
                allow_stretch=True,
                keep_ratio=False,
            )
        )

        self.create_buttons()
        self.create_labels()
        self.create_elements()

    def create_labels(self):
        settings_label = Label(
            text="Einstellungen",
            size_hint=(None, None),
            size=(50, 15),
            pos_hint={"x": 0.1, "y": 0.9},
            font_size=36,
            color=(0, 0, 0, 1),
        )
        brightness_label = Label(
            text="Helligkeit",
            size_hint=(None, None),
            size=(50, 15),
            pos_hint={"x": 0.08, "y": 0.75},
            font_size=32,
            color=(0, 0, 0, 1),
            halign="left",
        )
        dnd_label = Label(
            text="Ruhemodus",
            size_hint=(None, None),
            size=(50, 15),
            pos_hint={"x": 0.1, "y": 0.60},
            font_size=32,
            color=(0, 0, 0, 1),
            halign="left",
        )
        notification_label = Label(
            text="Nachrichten",
            size_hint=(None, None),
            size=(50, 15),
            pos_hint={"x": 0.1, "y": 0.45},
            font_size=32,
            color=(0, 0, 0, 1),
            halign="left",
        )
        wlan_label = Label(
            text="WLAN",
            size_hint=(None, None),
            size=(50, 15),
            pos_hint={"x": 0.06, "y": 0.30},
            font_size=32,
            color=(0, 0, 0, 1),
            halign="left",
        )

        self.add_widget(settings_label)
        self.add_widget(brightness_label)
        self.add_widget(dnd_label)
        self.add_widget(notification_label)
        self.add_widget(wlan_label)

    def create_buttons(self):
        button_home = Button(
            text="",
            size_hint=(None, None),
            size=(50, 50),
            pos_hint={"x": 0.93, "y": 0.88},
        )
        button_wlan_settings = Button(
            text="",
            size_hint=(None, None),
            size=(50, 50),
            pos_hint={"x": 0.32, "y": 0.27},
        )

        button_home.background_normal = "images/symbols/heim_tiny.png"
        button_home.background_down = "images/symbols/heim_tiny_pressed.png"
        button_wlan_settings.background_normal = "images/symbols/einstellungen_tiny.png"
        button_wlan_settings.background_down = (
            "images/symbols/einstellungen_tiny_pressed.png"
        )

        self.add_widget(button_home)
        self.add_widget(button_wlan_settings)

        button_home.bind(on_release=self.open_main_screen)

    def create_elements(self):
        slider = Slider(
            min=0,
            max=255,
            value=128,
            pos_hint={"x": 0.3, "y": 0.71},
            size_hint=(0.5, 0.1),
        )
        slider.bind(value=update_brightness)

        dnd_toggle = ToggleButton(
            text="OFF",
            size_hint=(None, None),
            size=(100, 50),
            pos_hint={"x": 0.3, "y": 0.57},
        )
        dnd_toggle.bind(state=toggle_switch)

        notification_toggle = ToggleButton(
            text="OFF",
            size_hint=(None, None),
            size=(100, 50),
            pos_hint={"x": 0.3, "y": 0.42},
        )
        notification_toggle.bind(state=toggle_switch)

        self.add_widget(slider)
        self.add_widget(dnd_toggle)
        self.add_widget(notification_toggle)

    def open_main_screen(self, instance):
        app = App.get_running_app()
        app.root.current = "main"


class ControlScreen(Screen):
    def __init__(self, **kwargs):
        super(ControlScreen, self).__init__(**kwargs)

        self.add_widget(
            Image(
                source="Images/gui/backgroud_base.png",
                allow_stretch=True,
                keep_ratio=False,
            )
        )

        self.create_labels()
        self.create_buttons()

    def create_labels(self):
        control_label = Label(
            text="Steuerung",
            size_hint=(None, None),
            size=(50, 15),
            pos_hint={"x": 0.1, "y": 0.9},
            font_size=36,
            color=(0, 0, 0, 1),
        )
        definition_label = Label(
            text="Bezeichnung",
            size_hint=(None, None),
            size=(50, 15),
            pos_hint={"x": 0.15, "y": 0.75},
            font_size=32,
            color=(0, 0, 0, 1),
        )
        status_label = Label(
            text="Status",
            size_hint=(None, None),
            size=(50, 15),
            pos_hint={"x": 0.6, "y": 0.75},
            font_size=32,
            color=(0, 0, 0, 1),
        )

        self.add_widget(control_label)
        self.add_widget(definition_label)
        self.add_widget(status_label)

    def create_buttons(self):
        button_home = Button(
            text="",
            size_hint=(None, None),
            size=(50, 50),
            pos_hint={"x": 0.93, "y": 0.88},
        )

        button_add = Button(
            text="Sensor Hinzufügen",
            size_hint=(None, None),
            size=(250, 50),
            pos_hint={"x": 0.375, "y": 0.20},
            font_size=24,
            color=(255, 255, 255, 1),
        )
        sensor1_button = Button(
            text="Sensor 1",
            size_hint=(None, None),
            size=(400, 50),
            pos_hint={"x": 0.08, "y": 0.60},
            font_size=32,
            color=(255, 255, 255, 1),
        )
        sensor2_button = Button(
            text="Sensor 2",
            size_hint=(None, None),
            size=(400, 50),
            pos_hint={"x": 0.08, "y": 0.50},
            font_size=32,
            color=(255, 255, 255, 1),
        )
        sensor1_status_button = Button(
            text="Online",
            size_hint=(None, None),
            size=(275, 50),
            pos_hint={"x": 0.575, "y": 0.60},
            font_size=32,
            color=(255, 255, 255, 1),
        )
        sensor2_status_button = Button(
            text="Batterie Schwach",
            size_hint=(None, None),
            size=(275, 50),
            pos_hint={"x": 0.575, "y": 0.50},
            font_size=32,
            color=(255, 255, 255, 1),
        )

        self.add_widget(button_home)
        self.add_widget(button_add)
        self.add_widget(sensor1_button)
        self.add_widget(sensor2_button)
        self.add_widget(sensor1_status_button)
        self.add_widget(sensor2_status_button)

        button_home.bind(on_release=self.open_main_screen)
        sensor1_button.bind(on_press=self.show_popup_sensor1)
        sensor2_button.bind(on_press=self.show_popup_sensor1)
        button_add.bind(on_press=self.show_popup_notimplemented)

        sensor1_button.background_normal = "images/gui/large_text_entry.png"
        sensor1_button.background_down = "images/gui/large_text_entry_pressed.png"
        sensor2_button.background_normal = "images/gui/large_text_entry.png"
        sensor2_button.background_down = "images/gui/large_text_entry_pressed.png"
        sensor1_status_button.background_normal = "images/gui/small_text_entry.png"
        sensor1_status_button.background_down = "images/gui/small_text_entry.png"
        sensor2_status_button.background_normal = "images/gui/small_text_entry.png"
        sensor2_status_button.background_down = "images/gui/small_text_entry.png"
        button_add.background_normal = "images/gui/large_text_entry.png"
        button_add.background_down = "images/gui/large_text_entry_pressed.png"
        button_home.background_normal = "images/symbols/heim_tiny.png"
        button_home.background_down = "images/symbols/heim_tiny_pressed.png"

    def open_main_screen(self, instance):
        app = App.get_running_app()
        app.root.current = "main"

    def show_popup_sensor1(self, instance):
        content = BoxLayout(orientation="vertical")
        label = Label(text="This is Sensor n \n UID:ui2nf8024fahf890", font_size=24)
        content.add_widget(label)

        popup = Popup(
            title="Information",
            content=content,
            size_hint=(None, None),
            size=(400, 400),
        )
        popup.open()
    
    def show_popup_notimplemented(self, instance):
        content = BoxLayout(orientation="vertical")
        label = Label(text="This Feature is not yet implemented", font_size=24)
        content.add_widget(label)

        popup = Popup(
            title="Information",
            content=content,
            size_hint=(None, None),
            size=(400, 400),
        )
        popup.open()


class ProfileScreen(Screen):
    def __init__(self, **kwargs):
        super(ProfileScreen, self).__init__(**kwargs)

        self.add_widget(
            Image(
                source="Images/gui/backgroud_base.png",
                allow_stretch=True,
                keep_ratio=False,
            )
        )
        self.create_labels()
        self.create_buttons()
        self.create_input_fields()

    def create_labels(self):
        profile_label = Label(
            text="Profil",
            size_hint=(None, None),
            size=(50, 15),
            pos_hint={"x": 0.05, "y": 0.9},
            font_size=36,
            color=(0, 0, 0, 1),
        )
        name_label = Label(
            text="Name:",
            size_hint=(None, None),
            size=(50, 15),
            pos_hint={"x": 0.05, "y": 0.75},
            font_size=32,
            color=(0, 0, 0, 1),
        )
        email_label = Label(
            text="Email:",
            size_hint=(None, None),
            size=(50, 15),
            pos_hint={"x": 0.05, "y": 0.625},
            font_size=32,
            color=(0, 0, 0, 1),
        )
        username_label = Label(
            text="Username:",
            size_hint=(None, None),
            size=(50, 15),
            pos_hint={"x": 0.08, "y": 0.50},
            font_size=32,
            color=(0, 0, 0, 1),
        )
        password_label = Label(
            text="Password:",
            size_hint=(None, None),
            size=(50, 15),
            pos_hint={"x": 0.08, "y": 0.375},
            font_size=32,
            color=(0, 0, 0, 1),
        )

        self.add_widget(profile_label)
        self.add_widget(name_label)
        self.add_widget(email_label)
        self.add_widget(username_label)
        self.add_widget(password_label)

    def create_buttons(self):
        button_home = Button(
            text="",
            size_hint=(None, None),
            size=(50, 50),
            pos_hint={"x": 0.93, "y": 0.88},
        )

        button_save = Button(
            text="Speichern",
            size_hint=(None, None),
            size=(150, 50),
            pos_hint={"x": 0.3, "y": 0.2},
            font_size=24,
            color=(255, 255, 255, 1),
        )

        self.add_widget(button_home)
        self.add_widget(button_save)

        button_home.bind(on_release=self.open_main_screen)
        button_save.bind(on_release=self.show_popup_save)

        button_home.background_normal = "images/symbols/heim_tiny.png"
        button_home.background_down = "images/symbols/heim_tiny_pressed.png"
        button_save.background_normal = "images/gui/small_text_entry_green.png"
        button_save.background_down = "images/gui/small_text_entry_green_pressed.png"

    def open_main_screen(self, instance):
        app = App.get_running_app()
        app.root.current = "main"

    def create_input_fields(self):
        name_input = TextInput(
            text="Enter Name",
            size_hint=(None, None),
            size=(500, 50),
            pos_hint={"x": 0.3, "y": 0.725},
            font_size=30,
            background_normal="images/gui/large_text_entry.png",
            background_active="images/gui/large_text_entry_pressed.png",
        )

        email_input = TextInput(
            text="Enter Email",
            size_hint=(None, None),
            size=(500, 50),
            pos_hint={"x": 0.3, "y": 0.6},
            font_size=30,
            background_normal="images/gui/large_text_entry.png",
            background_active="images/gui/large_text_entry_pressed.png",
        )

        username_input = TextInput(
            text="Enter Username",
            size_hint=(None, None),
            size=(500, 50),
            pos_hint={"x": 0.3, "y": 0.475},
            font_size=30,
            background_normal="images/gui/large_text_entry.png",
            background_active="images/gui/large_text_entry_pressed.png",
        )

        password_input = TextInput(
            text="",
            password=True,
            size_hint=(None, None),
            size=(500, 50),
            pos_hint={"x": 0.3, "y": 0.350},
            font_size=30,
            background_normal="images/gui/large_text_entry.png",
            background_active="images/gui/large_text_entry_pressed.png",
        )

        self.add_widget(name_input)
        self.add_widget(email_input)
        self.add_widget(username_input)
        self.add_widget(password_input)

    def show_popup_save(self, instance):
        content = BoxLayout(orientation="vertical")
        label = Label(text="Ihre Eingaben wurden gespeichert", font_size=24)
        content.add_widget(label)

        popup = Popup(
            title="Information",
            content=content,
            size_hint=(None, None),
            size=(400, 400),
        )
        popup.open()


def update_brightness(instance, value):
    set_screen_brightness(value)


def set_screen_brightness(brightness):
    brightness = max(0, min(brightness, 255))
    os.system(
        f"sudo sh -c 'echo {brightness} > /sys/class/backlight/rpi_backlight/brightness'"
    )


def toggle_switch(instance, value):
    if value == "normal":
        instance.text = "OFF"
        print("Switch is OFF")
    else:
        instance.text = "ON"
        print("Switch is ON")


class MyApp(App):
    def build(self):
        screen_manager = ScreenManager()
        Window.size = (1024, 600)
        Window.borderless = True

        splash_screen = SplashScreen(name="splash")
        screen_manager.add_widget(splash_screen)

        main_screen = HomeScreen(name="main")
        screen_manager.add_widget(main_screen)

        settings_screen = SettingsScreen(name="settings")
        screen_manager.add_widget(settings_screen)

        control_screen = ControlScreen(name="control")
        screen_manager.add_widget(control_screen)

        profile_screen = ProfileScreen(name="profile")
        screen_manager.add_widget(profile_screen)

        return screen_manager


if __name__ == "__main__":
    MyApp().run()
