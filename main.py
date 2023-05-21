
import PySimpleGUI as sg
from threading import Thread
from time import sleep

'''
Colour Definitions
'''
BG_STARTUP_SCREEN = '#FFFFFF'
TEXTC_STARTUP_SCREEN = '#5b5b5b'
FUNCTION_ELEMENT_COLOUR = '#3EB7F2'
FUNCTION_ELEMENT_COLOUR_2 = '#E5F6FE'
BLACK = '#000000'
WHITE = '#FFFFFF'

'''
Text Definitions
'''
FONT_MAIN = 'Calibri'

'''
Element Definitions
'''


# --- Startup Screen -------------------------------------------------
messages = iter([
    'Powering UP',
    'Sending Information to Skynet Host',
    'Initiation Permission Granted',
    'Security Protocols Engaged',
    'AP - Mines Armed',
    'Sentinel Drones Dispatched',
    'Perimeter Defense Established',
    'User Signatures Registered',
    'FOF System ACTIVE'])

def change_message():
    try:
        return next(messages)
    except StopIteration:
        return 'Praise to our Machine Overlords!'

# --- Simulated Counter -------------------------------------------------
bar_count = 0
active = True

def some_external_process():
    global bar_count, active
    while bar_count < 100:
        bar_count += 1
        sleep(0.1)
    active = False

# --- GUI --------------------------------------------------------------------
def splash_gui():
    layout = [
        [sg.Image(filename='images/logos/logo_small.png', key='LOGO', pad=(0,(30,5)), background_color=BG_STARTUP_SCREEN)],
        [sg.Text('Welcome to Skynet Home', justification='center', size=(50, 1),
                 text_color=TEXTC_STARTUP_SCREEN, font=(FONT_MAIN, 18), pad=((5, 5), (10, 25)), key='MSG',
                 background_color=BG_STARTUP_SCREEN)],
        [sg.Text('0%', size=(5, 1), text_color=TEXTC_STARTUP_SCREEN, font=(FONT_MAIN, 16), pad=((5, 5), (5, 12)),
                 key='PCT', background_color=BG_STARTUP_SCREEN)],
        [sg.ProgressBar(max_value=100, orientation='h', border_width=1, size=(25, 25),
                        bar_color=(FUNCTION_ELEMENT_COLOUR, WHITE), key='PRG')]
        ]

    return sg.Window('splash', layout, no_titlebar=True, element_justification='center',
                     size=(1024, 600), margins=(0, 0), alpha_channel=1, grab_anywhere=True, keep_on_top=True,
                     background_color=BG_STARTUP_SCREEN)

# --- Home Menu --------------------------------------------------------------------

def home_menu():
    left_col_layout = [
        [sg.Button('1')],
        [sg.Button('4')],
        [sg.Button('7')]
    ]

    middle_col_layout = [
        [sg.Image(filename='images\logos\logo_tiny.png', background_color=WHITE)],
        [sg.Button('5')],
        [sg.Button('8')]
    ]

    right_col_layout = [
        [sg.Image('images\symbols\\benutzer_small.png', background_color=WHITE), sg.Image('images\symbols\einstellungen_small.png', background_color=WHITE)],
        [sg.Button('6')],
        [sg.Button('9')]
    ]

    layout = [
        [sg.Column(left_col_layout, element_justification='left', expand_x=True, background_color=WHITE),
        sg.Column(middle_col_layout, element_justification='center', expand_x=True, background_color=WHITE),
        sg.Column(right_col_layout, element_justification='right', expand_x=True, background_color=WHITE)],
        ]

    return sg.Window('homescreen', layout, no_titlebar=True, element_justification='center',
                     size=(1024, 600), margins=(0, 0), alpha_channel=1, grab_anywhere=True, keep_on_top=True,
                     background_color=WHITE)

# --- Event Managemetn --------------------------------------------------------------------

def splash_screen_loop(window):
    global bar_count, active
    while active:
        window.read(100)
        window['PRG'].update_bar(current_count=bar_count)
        window['PCT'].update(value="{}%".format(bar_count))
        if bar_count%10 == 0:
            window['MSG'].update(value=change_message())

    window.read(2000)
    window.close()

def main_gui_loop(home_screen):
    home_screen.read(3000)
    home_screen.close()

def main():
    t1 = Thread(target=some_external_process)
    t1.start()
    splash_screen = splash_gui()
    splash_screen_loop(splash_screen)
    home_screen = home_menu()
    main_gui_loop(home_screen)



if __name__=='__main__':
    main()
