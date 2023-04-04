import tkinter as tk
from tkinter import ttk


def button_func():
    print("A button was pressed")


def hello_func():
    print("hello")


# create a window
window = tk.Tk()
window.title("Window and Widgets")
window.geometry("800x500")

# ttk.Label
label = ttk.Label(master=window, text="This is a test")
label.pack()

# tk.Text
text = tk.Text(master=window)
text.pack()

# ttk.Entry
entry = ttk.Entry(master=window)
entry.pack()

# Exercise
exercise_label = ttk.Label(master=window, text="my label")
exercise_label.pack()
# exercise_button = ttk.Button(master=window, text="exercise button", command=hello_func)
exercise_button = ttk.Button(
    master=window, text="exercise button", command=lambda: print("hello")
)
exercise_button.pack()

# ttk.Button
button = ttk.Button(master=window, text="A button", command=button_func)
button.pack()

# run
window.mainloop()
