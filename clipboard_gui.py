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


    def label_click(self, event):
        clicked_label = event.widget
        pyperclip.copy(clicked_label["text"])
        self.close()


    def create_labels(self):
        for element in self.elements:
            label = tk.Label(self.root, text=element, font=('Arial', 12), padx=10, pady=6, relief=tk.RAISED)
            label.pack(fill=tk.X)  # Make the label expand horizontally
            label.bind('<Button-1>', self.label_click)


    def run(self):
        self.root.mainloop()


    def close(self):
        self.root.destroy()