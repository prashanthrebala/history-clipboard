from clipboard_gui import ClipboardGUI
from pynput import keyboard

import json
import pyperclip
import os


file_path = '/home/talon97/Code/history-clipboard/clippy/data.json'

clipboard_history = []

def safe_open_w(path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    return open(path, 'w')

def on_ctrl_c():
    clipboard_history.append(pyperclip.paste())
    with safe_open_w(file_path) as file:
        json.dump(clipboard_history, file, indent=2)

def open_history():
    cgui = ClipboardGUI(clipboard_history)
    cgui.run()


listener = keyboard.GlobalHotKeys({
    '<ctrl>+c': on_ctrl_c,
    '<ctrl>+<alt>+c': open_history,
})


if __name__ == "__main__":
    if os.path.isfile(file_path):
        with open(file_path, 'r') as file:
            clipboard_history = json.load(file)
    listener.start()
    listener.join()

