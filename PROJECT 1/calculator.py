import tkinter as tk
from tkinter import font

# Функціонал

def button_click(value):
    """Додає значення до поля вводу."""
    if entry_result.get() != "":
        entry_result.delete(0, tk.END)
        entry_result.insert(tk.END, "")
    current = entry.get()
    if current == "0":
        entry.delete(0, tk.END)
    entry.insert(tk.END, value)


def clear():
    """Очищує поле вводу та результату."""
    entry.delete(0, tk.END)
    entry.insert(0, "0")
    entry_result.delete(0, tk.END)
    entry_result.insert(0, "")


def add():
    """Операція додавання."""
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + "+")


def subtract():
    """Операція віднімання."""
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + "-")


def multiply():
    """Операція множення."""
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + "x")


def divide():
    """Операція ділення."""
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + "÷")


def mod():
    """Операція залишок від ділення."""
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + "%")


def calculate():
    """Обчислює результат виразу."""
    try:
        expression = entry.get()
        display_expression = expression.replace('*', 'x').replace('/', '÷')
        result = eval(expression.replace('x', '*').replace('÷', '/'))
        entry_result.config(font=segoe_small_font, fg="light gray")
        entry_result.delete(0, tk.END)
        entry_result.insert(tk.END, display_expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")


def backspace():
    """Видаляє останній символ."""
    current = entry.get()
    if len(current) > 1:
        entry.delete(len(current)-1, tk.END)
    else:
        entry.delete(0, tk.END)
        entry.insert(0, "0")


# Дизайн

root = tk.Tk()
root.title("Calculator")
root.config(bg="#FFFFFF")

# Встановлення шрифту Segoe UI
segoe_font = font.Font(family="Segoe UI", size=18)
segoe_small_font = font.Font(family="Segoe UI", size=14)

# Створення поля для виразу
entry_result = tk.Entry(
    root, font=segoe_small_font, borderwidth=0, relief=tk.FLAT,
    justify='right', bg="#FFFFFF", fg="light gray"
)
entry_result.grid(row=0, column=0, columnspan=4, pady=(10, 0), padx=5, sticky="nsew")

# Створення поля для результату
entry = tk.Entry(
    root, font=segoe_font, borderwidth=0, relief=tk.FLAT, 
    justify='right', bg="#FFFFFF"
)
entry.grid(row=1, column=0, columnspan=4, pady=(0, 10), padx=5, sticky="nsew")
entry.insert(0, "0")

# Стилі кнопок
button_bg = "#f0f0f0"
button_fg = "#000000"
button_active_bg = "#d0d0d0"
button_font = segoe_font
button_width = 7
button_height = 2
dark_gray_bg = "#a9a9a9"

# Створення кнопок
buttons = [
    ('C', 2, 0, clear), ('÷', 2, 1, divide), ('%', 2, 2, mod), ('←', 2, 3, backspace),
    ('7', 3, 0, button_click), ('8', 3, 1, button_click), ('9', 3, 2, button_click), ('x', 3, 3, multiply),
    ('4', 4, 0, button_click), ('5', 4, 1, button_click), ('6', 4, 2, button_click), ('-', 4, 3, subtract),
    ('1', 5, 0, button_click), ('2', 5, 1, button_click), ('3', 5, 2, button_click), ('+', 5, 3, add),
    ('0', 6, 0, button_click), ('.', 6, 2, button_click), ('=', 6, 3, calculate)
]

for (text, row, col, command) in buttons:
    if text:
        button = tk.Button(
            root, text=text, font=button_font, 
            bg=dark_gray_bg if text in ['C', '÷', '%'] else 
            (button_bg if text not in ['+', '-', 'x', '=', '←'] else "#00ff00"), 
            fg=button_fg, activebackground=button_active_bg, width=button_width, 
            height=button_height, command=lambda t=text, cmd=command: cmd(t) if cmd == button_click else cmd(), 
            bd=0, highlightthickness=0
        )
        button.grid(row=row, column=col, sticky="nsew", padx=0, pady=0)

# Розтягування кнопок і поля вводу
for i in range(7):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()
