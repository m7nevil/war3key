# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import keyboard
import psutil
from threading import Timer
import win32gui
import win32process
from pykeyboard import PyKeyboard

is_active = False
k = PyKeyboard()


def tap_num(num):
    return lambda e: k.tap_key(k.numpad_keys[num])


def check_process(name):
    try:
        window = win32gui.GetForegroundWindow()
        pids = win32process.GetWindowThreadProcessId(window)
        proc_name = psutil.Process(pids[-1]).name()
    except:
        proc_name = ''

    return name == proc_name


def check_focused(name):
    global is_active
    active = check_process(name)

    if active != is_active:
        print('KeyMap On' if active else 'KeyMap Off')

    if active:
        if not is_active:
            keyboard.on_press_key('q', tap_num(7), True)
            keyboard.on_press_key('~', tap_num(8), True)
            keyboard.on_press_key('capslock', tap_num(4), True)
            keyboard.on_press_key('left win', lambda: 0, True)
            is_active = True
    else:
        keyboard.unhook_all()
        is_active = False

    t = Timer(5, check_focused, [name])
    t.start()


print('Started...')
check_focused('Warcraft III.exe')
keyboard.wait()
