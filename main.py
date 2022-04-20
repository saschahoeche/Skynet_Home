
import PySimpleGUI as sg
from threading import Thread
from time import sleep

images = ['Images/logo_small.png']
img_iter = iter(images)

messages = iter([
    'Powering UP',
    'Sending Information to local Machine Host',
    'Security Protocols established',
    'Perimeter Defense established',
    'Bulletstorm Anti Personnel Equipment connected',
    'Internal Life Signatures Registered'])

def change_message():
    try:
        return next(messages)
    except StopIteration:
        return 'Praise the Machine Overlords!'

def animate_water():
    global img_iter, images
    try:
        return next(img_iter)
    except StopIteration:
        img_iter = iter(images)
        return next(img_iter)

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
        [sg.Image(filename='Images/logo_small.png', key='WATER', pad=(0,(30,0)))],
        [sg.Text('', justification='center', text_color='#00a2e8', font=('Tahoma', 30), pad=((5, 5), (25, 5)))],
        [sg.Text('Welcome to Skynet Home', justification='center', size=(50, 1),
                text_color='#5b5b5b', font=('Tahoma', 18), pad=((5, 5), (10, 25)), key='MSG')],
        [sg.Text('0%', size=(5, 1), text_color='#5b5b5b', font=('Tahoma', 16), pad=((5, 5), (5, 12)), key='PCT')],
        [sg.Image('', key='BOAT')],
        [sg.ProgressBar(max_value=100, orientation='h', border_width=1, size=(25, 25),
                        bar_color=('#00a2e8', '#FFFFFF'), key='PRG')]
        ]

    return sg.Window('splash', layout, no_titlebar=True, element_justification='center',
        size=(1024, 600), margins=(0, 0), alpha_channel=1, grab_anywhere=True, keep_on_top=True)

def gui_event_loop(window):
    global bar_count, active
    while active:
        window.read(100)
        window['PRG'].update_bar(current_count=bar_count)
        window['PCT'].update(value="{}%".format(bar_count))
        if bar_count%10 == 0:
            window['MSG'].update(value=change_message())
        if bar_count%4 == 0:
            window['WATER'].update(filename=animate_water())

    # window['PRG'].update(visible=False)
    # window['PCT'].update(visible=False)
    # window['WATER'].update(visible=False)
    # window['MSG'].update(font=('Tahoma', 12, 'bold'))
    # window['BOAT'].update(filename='Images/logo_small.png')
    window.read(3000)
    window.close()

def main():
    t1 = Thread(target=some_external_process)
    t1.start()
    window = splash_gui()
    gui_event_loop(window)

if __name__=='__main__':
    main()
