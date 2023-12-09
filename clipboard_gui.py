from utils.text_processor import truncate_text

import tkinter as tk
import pyperclip

class ClipboardGUI:
    def __init__(self, elements):
        self.elements = elements
        self.root = tk.Tk()
        self.root.title("Clipboard History")
        self.root.resizable(width=False, height=False)

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        window_width = 200
        window_height = 33 * len(self.elements)
        window_x = screen_width - window_width
        window_y = screen_height - window_height

        self.root.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")
        self.create_labels()


    def label_click(self, text):
        pyperclip.copy(text)
        self.close()


    def create_labels(self):
        max_length = 20
        for element in self.elements:
            label = tk.Label(self.root, text=truncate_text(element, max_length), font=('Arial', 11), padx=10, pady=7, relief=tk.RAISED)
            label.pack(fill=tk.X)  # Make the label expand horizontally
            label.bind('<Button-1>', lambda: self.label_click(element))


    def run(self):
        self.root.mainloop()


    def close(self):
        self.root.destroy()