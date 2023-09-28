import tkinter as tk
from tkinter.ttk import *
def submit():
    option = combo.get()
    lbl["text"] = option
window = tk.Tk()
combo = Combobox(window)
combo['values'] = ("IN", "CA", "MA")
btn = tk.Button(window, text="Submit", command=submit)
lbl = tk.Label(window)
combo.grid(column=0, row=0)
btn.grid(column=1, row=0)
lbl.grid(column=2, row=0)
window.mainloop()