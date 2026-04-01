import tkinter as tk
from tkinter import messagebox
import math

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Calculator')
        self.geometry('400x600')
        self.create_widgets()

    def create_widgets(self):
        # Entry for input
        self.entry = tk.Entry(self, font=('Arial', 24), bd=10, insertwidth=2, width=14, borderwidth=4)
        self.entry.grid(row=0, column=0, columnspan=4)

        # Buttons for basic operations
        buttons = [
            '7', '8', '9', '/','
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'C', 'sin', 'cos', 'tan',
            '√', 'log', 'exp', 'history']

        row_val = 1
        col_val = 0
        for button in buttons:
            action = lambda x=button: self.click_event(x)
            tk.Button(self, text=button, padx=20, pady=20, font=('Arial', 18), command=action).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val == 4:
                col_val = 0
                row_val += 1

        # Theme buttons
        self.light_theme = tk.Button(self, text='Light Theme', command=self.light_theme)
        self.light_theme.grid(row=row_val, column=0)
        self.dark_theme = tk.Button(self, text='Dark Theme', command=self.dark_theme)
        self.dark_theme.grid(row=row_val, column=1)

    def click_event(self, key):
        if key == 'C':
            self.entry.delete(0, tk.END)
        elif key == '=':
            try:
                self.entry.insert(tk.END, '=' + str(eval(self.entry.get())))
            except Exception:
                messagebox.showerror('Error', 'Invalid Input')
        elif key in ('sin', 'cos', 'tan', '√', 'log', 'exp'):
            try:
                if key == 'sin':
                    self.entry.insert(tk.END, math.sin(math.radians(float(self.entry.get()))))
                elif key == 'cos':
                    self.entry.insert(tk.END, math.cos(math.radians(float(self.entry.get()))))
                elif key == 'tan':
                    self.entry.insert(tk.END, math.tan(math.radians(float(self.entry.get()))))
                elif key == '√':
                    self.entry.insert(tk.END, math.sqrt(float(self.entry.get())))
                elif key == 'log':
                    self.entry.insert(tk.END, math.log(float(self.entry.get())))
                elif key == 'exp':
                    self.entry.insert(tk.END, math.exp(float(self.entry.get())))
                self.entry.delete(0, tk.END)
            except Exception:
                messagebox.showerror('Error', 'Invalid Input')
        else:
            self.entry.insert(tk.END, key)

    def light_theme(self):
        self.config(bg='white')
        self.entry.config(bg='lightgrey')

    def dark_theme(self):
        self.config(bg='black')
        self.entry.config(bg='darkgrey')

if __name__ == '__main__':
    app = Calculator()
    app.mainloop()