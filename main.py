from pynput import keyboard
import pyperclip
import os

file_path = '/home/talon97/Code/history-clipboard/clippy/data.txt'

clipboard_history = []

def safe_open_w(path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    return open(path, 'w')

def on_ctrl_c():
    print(pyperclip.paste())
    clipboard_history.append(pyperclip.paste())
    with safe_open_w(file_path) as file:
        file.writelines(clipboard_history)


listener = keyboard.GlobalHotKeys({
    '<ctrl>+c': on_ctrl_c,
})

listener.start()

listener.join()

