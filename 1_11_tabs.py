import tkinter as tk
from tkinter import ttk


# window
window = tk.Tk()
window.geometry("600x400")
window.title("Tab Widget")

# Notebook widget
notebook = ttk.Notebook(window)

# tab 1
tab1 = ttk.Frame(notebook)
label1 = ttk.Label(tab1, text="Text in tab 1")
label1.pack()
button1 = ttk.Button(tab1, text="Button in tab 1")
button1.pack()

# tab 2
tab2 = ttk.Frame(notebook)
label2 = ttk.Label(tab2, text="Text in tab 2")
label2.pack()
entry2 = ttk.Entry(tab2)
entry2.pack()

notebook.add(tab1, text="Tab 1")
notebook.add(tab2, text="Tab 2")
notebook.pack()

# Exercise
exercise_tab = ttk.Frame(notebook)
exercise_button_1 = ttk.Button(exercise_tab, text="button 1")
exercise_button_1.pack()
exercise_button_2 = ttk.Button(exercise_tab, text="button 2")
exercise_button_2.pack()
exercise_label_2 = ttk.Label(exercise_tab, text="Label")
exercise_label_2.pack()

notebook.add(exercise_tab, text="Exercise Tab")

# run
window.mainloop()
