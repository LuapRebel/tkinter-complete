import tkinter as tk
from tkinter import ttk


def button_func():
    # get contents of entry
    entry_text = entry.get()

    # update label
    # label.configure(text="some other text")
    label["text"] = entry_text
    entry["state"] = "disabled"
    # print(label.configure())


def reset_func():
    label["text"] = "some text"
    entry["state"] = "enabled"


# window
window = tk.Tk()
window.title("Getting and setting widgets")

# widgets
label = ttk.Label(master=window, text="Some text")
label.pack()
entry = ttk.Entry(master=window)
entry.pack()
button = ttk.Button(master=window, text="The button", command=button_func)
button.pack()
exercise_button = ttk.Button(
    master=window, text="change to some text", command=reset_func
)
exercise_button.pack()

# run
window.mainloop()
