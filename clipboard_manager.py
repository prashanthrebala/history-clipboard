from clipboard_gui import ClipboardGUI
from pynput import keyboard

import json
import pyperclip
import os


class ClipboardManager():

    def __init__(self, file_path):
        self.clipboard_history = []
        self.file_path = file_path

    def safe_open_w(self, path):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        return open(path, 'w')

    def on_ctrl_c(self):
        clipboard_item = pyperclip.paste()
        if clipboard_item == "" or len(self.clipboard_history) and clipboard_item == self.clipboard_history[-1]:
            return
        self.clipboard_history.append(clipboard_item)
        self.clipboard_history = self.clipboard_history[-10:] # limit to 10 entries
        with self.safe_open_w(self.file_path) as file:
            json.dump(self.clipboard_history, file, indent=2)

    def open_history(self):
        cgui = ClipboardGUI(self.clipboard_history[::-1])
        cgui.run()

    def load_history_from_file(self):
        if os.path.isfile(self.file_path):
            with open(self.file_path, 'r') as file:
                self.clipboard_history = json.load(file)

    def start_listener(self):
        listener = keyboard.GlobalHotKeys({
            '<ctrl>+c': self.on_ctrl_c,
            '<ctrl>+<alt>+c': self.open_history,
        })
        listener.start()
        print("History clipboard started")
        listener.join()