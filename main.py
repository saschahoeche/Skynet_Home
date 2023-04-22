
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


images = ['Images/logo_small.png']
img_iter = iter(images)

messages = iter([
    'Powering UP',
    'Sending Information to Skynet Host',
    'Initiation permission granted',
    'Security Protocols Established',
    'AP - Mines armed',
    'Sentinel Drones Dispatched',
    'Perimeter Defense Established',
    'User Signatures Registered',
    'FOF System active'])

def change_message():
    try:
        return next(messages)
    except StopIteration:
        return 'Praise to our Machine Overlords!'

# --- SOME SIMULATED PROCESS -------------------------------------------------
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
        [sg.Image(filename='Images/logo_small.png', key='LOGO', pad=(0,(30,5)), background_color=BG_STARTUP_SCREEN)],
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

def gui_event_loop(window):
    global bar_count, active
    while active:
        window.read(100)
        window['PRG'].update_bar(current_count=bar_count)
        window['PCT'].update(value="{}%".format(bar_count))
        if bar_count%10 == 0:
            window['MSG'].update(value=change_message())

    window.read(3000)
    window.close()

def main():
    t1 = Thread(target=some_external_process)
    t1.start()
    window = splash_gui()
    gui_event_loop(window)

if __name__=='__main__':
    main()
