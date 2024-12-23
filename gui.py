import tkinter as tk
from tkinter import scrolledtext

class ShellGUI:
    def __init__(self, shell):
        self.shell = shell
        self.root = tk.Tk()
        self.root.title("Shell Emulator")
        self.text_area = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, width=80, height=20)
        self.text_area.pack()
        self.entry = tk.Entry(self.root, width=80)
        self.entry.bind("<Return>", self.execute_command)
        self.entry.pack()

    def execute_command(self, event):
        command = self.entry.get()
        self.entry.delete(0, tk.END)
        output = self.shell.execute_command(command)
        if output == "exit":
            self.root.quit()
        self.text_area.insert(tk.END, f"{self.shell.prompt()}{command}\n{output}\n")

    def run(self):
        self.root.mainloop()
