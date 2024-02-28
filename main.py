"""
Manual run module
"""
from pynput import keyboard
from replay_wizard.capturing.keyboard import on_press


with keyboard.Listener(
                on_press=on_press
) as listener:
    listener.join()
